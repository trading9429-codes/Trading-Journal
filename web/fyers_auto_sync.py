#!/usr/bin/env python3
"""
FYERS Automated Zero-Prompt Live Sync Bridge
Trader Execution Reset System &bull; Intraday 1-Minute Equities (NSE)

Features:
- Pure Python RFC 6238 TOTP computation (Zero third-party pip dependencies)
- 1-Step automated login: Generates TOTP -> Authenticates session -> Gets Access Token
- Auto-syncs today's tradebook fills, calculates FYERS statutory costs, updates Excel
- Emergency 1-click broker kill switch support
"""

import os
import sys
import json
import time
import base64
import hmac
import hashlib
import struct
import urllib.request
import urllib.parse
from datetime import datetime

# Local imports
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, ".fyers_config.json")
TOKEN_FILE = os.path.join(BASE_DIR, ".fyers_token.json")

from fyers_bridge import (
    load_config, save_config, save_token, load_token,
    compute_fyers_charges, sync_trades_to_system,
    trigger_physical_kill_switch, send_telegram_alert
)

def generate_totp_code(secret):
    """Generates 6-digit TOTP code using pure Python standard library (RFC 6238)."""
    cleaned_secret = secret.upper().replace(" ", "").strip()
    # Pad base32 string if needed
    missing_padding = len(cleaned_secret) % 8
    if missing_padding != 0:
        cleaned_secret += '=' * (8 - missing_padding)
    key = base64.b32decode(cleaned_secret, casefold=True)
    counter = int(time.time() // 30)
    msg = struct.pack(">Q", counter)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    offset = h[-1] & 0x0F
    code = (struct.unpack(">I", h[offset:offset + 4])[0] & 0x7FFFFFFF) % 1000000
    return f"{code:06d}"

def auto_login_and_sync(cfg):
    """
    Performs automated zero-prompt login with stored credentials and syncs tradebook.
    """
    app_id = cfg.get("app_id")
    secret_key = cfg.get("secret_key")
    fy_id = cfg.get("fy_id")
    pin = cfg.get("pin")
    totp_key = cfg.get("totp_key")

    # If already have a valid token from today, try it first
    cached_token = load_token()
    if cached_token:
        try:
            print("Testing cached access token...")
            count = sync_trades_to_system(cached_token, cfg)
            print(f"✅ Live sync completed using cached session! ({count} fills processed)")
            return cached_token
        except Exception as e:
            print(f"Cached token expired or invalid ({e}). Regenerating token automatically...")

    if not totp_key or not pin or not fy_id:
        print("\n=== Automated FYERS Credentials Setup (One-Time) ===")
        fy_id = input(f"Enter FYERS User ID / Client ID [{cfg.get('fy_id', '')}]: ") or cfg.get("fy_id", "")
        pin = input(f"Enter 4-digit FYERS PIN [{cfg.get('pin', '')}]: ") or cfg.get("pin", "")
        totp_key = input("Enter TOTP Secret Key (from Google Authenticator 2FA setup): ").strip()
        app_id = input(f"Enter App ID [{cfg.get('app_id', '')}]: ") or cfg.get("app_id", "")
        secret_key = input(f"Enter Secret Key [{cfg.get('secret_key', '')}]: ") or cfg.get("secret_key", "")

        cfg.update({
            "fy_id": fy_id,
            "pin": pin,
            "totp_key": totp_key,
            "app_id": app_id,
            "secret_key": secret_key
        })
        save_config(cfg)

    # 1. Generate 6-digit TOTP
    totp_code = generate_totp_code(totp_key)
    print(f"🔐 Generated live TOTP: {totp_code}")

    # 2. Automated FYERS login flow via API v3
    # Step A: Send TOTP verification
    print("Authenticating session with FYERS API...")
    totp_payload = json.dumps({"fy_id": fy_id, "app_id": "2", "otp": totp_code}).encode("utf-8")
    req = urllib.request.Request(
        "https://api-t2.fyers.in/vagator/v2/verify_otp",
        data=totp_payload,
        headers={"Content-Type": "application/json"}
    )
    request_key = ""
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            request_key = data.get("request_key")
    except Exception as e:
        print(f"[Warning] Direct TOTP endpoint notice: {e}")

    # Step B: Verify PIN if request_key obtained
    if request_key:
        pin_payload = json.dumps({"identity_type": "pin", "identifier": pin, "request_key": request_key}).encode("utf-8")
        req_pin = urllib.request.Request(
            "https://api-t2.fyers.in/vagator/v2/verify_pin",
            data=pin_payload,
            headers={"Content-Type": "application/json"}
        )
        try:
            with urllib.request.urlopen(req_pin, timeout=10) as resp:
                data_pin = json.loads(resp.read().decode("utf-8"))
                token = data_pin.get("data", {}).get("access_token")
                if token:
                    save_token(token)
                    print("✅ Automated login successful! Daily access token obtained.")
                    sync_trades_to_system(token, cfg)
                    return token
        except Exception as e:
            print(f"[Notice] PIN verification response: {e}")

    # If automated endpoint is restricted by FYERS IP policy, fallback to manual token paste
    print("\n💡 Fallback: Paste today's access token from FYERS Web / API dashboard:")
    manual_token = input("Enter Access Token: ").strip()
    if manual_token:
        save_token(manual_token)
        sync_trades_to_system(manual_token, cfg)
        return manual_token

def main():
    import argparse
    parser = argparse.ArgumentParser(description="FYERS Automated Zero-Prompt Live Sync Bridge")
    parser.add_argument("--sync", action="store_true", help="Perform automated TOTP login and sync fills")
    parser.add_argument("--kill-switch", action="store_true", help="Execute emergency auto-square off and cancel orders")
    args = parser.parse_args()

    cfg = load_config()
    if args.kill_switch:
        token = load_token()
        if not token:
            print("No active token found to execute kill switch.")
            sys.exit(1)
        res = trigger_physical_kill_switch(token, cfg)
        print("Broker kill switch executed:", res)
        return

    print("=== FYERS Automated Zero-Prompt Live Sync ===")
    auto_login_and_sync(cfg)

if __name__ == "__main__":
    main()

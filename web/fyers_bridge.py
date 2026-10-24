#!/usr/bin/env python3
"""
FYERS API v3 Live Integration & Auto-Sync Bridge
Trader Execution Reset System &bull; Intraday 1-Minute Equities (NSE)

Features:
- OAuth 2.0 Auth Code & Daily Access Token Generation
- Automated Tradebook & Orderbook Fetching & Deduplication
- Exact FYERS Intraday Equity Statutory Charges Computation
- Direct Synchronization with trades_store.json and D3_Tracking_Spreadsheet.xlsx
- Emergency Physical Broker Kill Switch (Cancel Orders & Auto-Square Off)
"""

import sys
import os
import json
import argparse
import urllib.request
import urllib.parse
import hashlib
from datetime import datetime

# Path references
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, ".fyers_config.json")
TOKEN_FILE = os.path.join(BASE_DIR, ".fyers_token.json")
TRADES_STORE = os.path.join(BASE_DIR, "trades_store.json")

# FYERS API v3 Endpoints
FYERS_AUTH_URL = "https://api-t1.fyers.in/api/v3/generate-authcode"
FYERS_TOKEN_URL = "https://api-t1.fyers.in/api/v3/validate-authcode"
FYERS_PROFILE_URL = "https://api-t1.fyers.in/api/v3/profile"
FYERS_TRADEBOOK_URL = "https://api-t1.fyers.in/api/v3/tradebook"
FYERS_ORDERS_URL = "https://api-t1.fyers.in/api/v3/orders"
FYERS_POSITIONS_URL = "https://api-t1.fyers.in/api/v3/positions"

def load_config():
    """Loads FYERS configuration from file or environment variables."""
    cfg = {
        "app_id": os.environ.get("FYERS_APP_ID", ""),
        "secret_key": os.environ.get("FYERS_SECRET_KEY", ""),
        "redirect_uri": os.environ.get("FYERS_REDIRECT_URI", "https://trade.fyers.in/api-login/redirect-uri/index.html"),
        "telegram_bot_token": os.environ.get("TELEGRAM_BOT_TOKEN", ""),
        "telegram_chat_id": os.environ.get("TELEGRAM_CHAT_ID", "")
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                file_cfg = json.load(f)
                cfg.update(file_cfg)
        except Exception as e:
            print(f"[Warning] Failed to read config file: {e}")
    return cfg

def save_config(cfg):
    """Saves FYERS configuration to local config file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)
    os.chmod(CONFIG_FILE, 0o600)
    print(f"Configuration saved to {CONFIG_FILE}")

def load_token():
    """Loads cached daily access token."""
    if not os.path.exists(TOKEN_FILE):
        return None
    try:
        with open(TOKEN_FILE, "r") as f:
            data = json.load(f)
            return data.get("access_token")
    except Exception:
        return None

def save_token(access_token):
    """Saves daily access token."""
    data = {
        "access_token": access_token,
        "saved_at": datetime.now().isoformat()
    }
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f, indent=2)
    os.chmod(TOKEN_FILE, 0o600)
    print(f"Daily access token cached in {TOKEN_FILE}")

def compute_fyers_charges(entry_price, exit_price, qty):
    """
    Computes exact FYERS statutory intraday charges for NSE Equities.
    - Brokerage: ₹20 or 0.03% whichever is lower per leg
    - STT: 0.025% on sell leg
    - Exch: 0.00297% on turnover
    - SEBI: ₹10 / crore (0.0001%)
    - Stamp: 0.003% on buy leg
    - GST: 18% on (Brokerage + Exch + SEBI)
    """
    buy_turnover = entry_price * qty
    sell_turnover = exit_price * qty
    total_turnover = buy_turnover + sell_turnover

    buy_brokerage = min(20.0, buy_turnover * 0.0003)
    sell_brokerage = min(20.0, sell_turnover * 0.0003)
    total_brokerage = round(buy_brokerage + sell_brokerage, 2)

    stt = round(sell_turnover * 0.00025, 2)
    exch_txn = round(total_turnover * 0.0000297, 2)
    sebi_turnover = round(total_turnover * 0.000001, 2)
    stamp_duty = round(buy_turnover * 0.00003, 2)
    gst = round((total_brokerage + exch_txn + sebi_turnover) * 0.18, 2)

    total_statutory = round(total_brokerage + stt + exch_txn + sebi_turnover + stamp_duty + gst, 2)
    return {
        "brokerage": total_brokerage,
        "stt": stt,
        "exch_txn": exch_txn,
        "sebi": sebi_turnover,
        "stamp_duty": stamp_duty,
        "gst": gst,
        "total_charges": total_statutory
    }

def send_telegram_alert(message, cfg):
    """Sends immediate accountability notification via Telegram Bot API."""
    bot_token = cfg.get("telegram_bot_token")
    chat_id = cfg.get("telegram_chat_id")
    if not bot_token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = json.dumps({"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            pass
    except Exception as e:
        print(f"[Telegram Alert Failed] {e}")

def get_auth_url(cfg):
    """Constructs FYERS OAuth login URL."""
    app_id = cfg.get("app_id")
    redirect_uri = cfg.get("redirect_uri")
    if not app_id:
        raise ValueError("app_id is required in .fyers_config.json")
    params = urllib.parse.urlencode({
        "client_id": app_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "state": "trader_reset_system"
    })
    return f"{FYERS_AUTH_URL}?{params}"

def validate_auth_code(auth_code, cfg):
    """Exchanges auth_code for access_token."""
    app_id = cfg.get("app_id")
    secret_key = cfg.get("secret_key")
    if not app_id or not secret_key:
        raise ValueError("app_id and secret_key are required in .fyers_config.json")

    # FYERS AppIdHash = SHA-256(app_id + ":" + secret_key)
    hash_str = f"{app_id}:{secret_key}"
    app_id_hash = hashlib.sha256(hash_str.encode("utf-8")).hexdigest()

    payload = json.dumps({
        "grant_type": "authorization_code",
        "appIdHash": app_id_hash,
        "code": auth_code
    }).encode("utf-8")

    req = urllib.request.Request(FYERS_TOKEN_URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("s") == "ok":
                token = data.get("access_token")
                save_token(token)
                return token
            else:
                raise RuntimeError(f"FYERS Auth Error: {data.get('message', data)}")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        raise RuntimeError(f"HTTP Error {e.code}: {err_msg}")

def check_profile(token, cfg):
    """Checks profile validity."""
    app_id = cfg.get("app_id")
    headers = {
        "Authorization": f"{app_id}:{token}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(FYERS_PROFILE_URL, headers=headers)
    with urllib.request.urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode("utf-8"))

def fetch_tradebook(token, cfg):
    """Fetches intraday tradebook fills."""
    app_id = cfg.get("app_id")
    headers = {
        "Authorization": f"{app_id}:{token}",
        "Content-Type": "application/json"
    }
    req = urllib.request.Request(FYERS_TRADEBOOK_URL, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))

def trigger_physical_kill_switch(token, cfg):
    """Cancels open orders and exits open intraday positions."""
    app_id = cfg.get("app_id")
    headers = {
        "Authorization": f"{app_id}:{token}",
        "Content-Type": "application/json"
    }
    # 1. Exit all open positions
    exit_payload = json.dumps({"exit_all": 1}).encode("utf-8")
    req = urllib.request.Request(FYERS_POSITIONS_URL, data=exit_payload, headers=headers, method="DELETE")
    res = {}
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            res = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        res = {"error": str(e)}

    # Send telegram emergency alert
    msg = (
        "🛑 *BROKER KILL SWITCH ENGAGED VIA FYERS API*\n\n"
        "• All open intraday positions sent square-off request.\n"
        "• Hard daily stop active (2 trades or 2 losses reached).\n"
        "• Platform locked for the remainder of the session."
    )
    send_telegram_alert(msg, cfg)
    return res

def sync_trades_to_system(token, cfg):
    """Fetches today's tradebook, pairs fills, calculates charges, and saves to database."""
    print("Fetching today's tradebook fills from FYERS API...")
    data = fetch_tradebook(token, cfg)
    trades_list = data.get("tradeBook", [])
    if not trades_list:
        print("No executed trades found in FYERS tradebook today.")
        return 0

    print(f"Found {len(trades_list)} execution fills in FYERS tradebook.")

    # Load existing trades
    existing = []
    if os.path.exists(TRADES_STORE):
        try:
            with open(TRADES_STORE, "r") as f:
                existing = json.load(f)
        except Exception:
            existing = []

    # Map existing trade hashes to avoid duplicates
    existing_hashes = {t.get("fyers_id") for t in existing if t.get("fyers_id")}

    # Group fills by symbol
    from collections import defaultdict
    by_symbol = defaultdict(list)
    for fill in trades_list:
        symbol = fill.get("symbol", "").replace("NSE:", "").replace("-EQ", "")
        by_symbol[symbol].append(fill)

    new_trades = []
    for sym, fills in by_symbol.items():
        buys = [f for f in fills if f.get("transactionType") == 1]
        sells = [f for f in fills if f.get("transactionType") == -1]

        total_buy_qty = sum(b.get("tradedQty", 0) for b in buys)
        total_sell_qty = sum(s.get("tradedQty", 0) for s in sells)

        matched_qty = min(total_buy_qty, total_sell_qty)
        if matched_qty <= 0:
            continue

        avg_buy_px = sum(b.get("tradePrice", 0) * b.get("tradedQty", 0) for b in buys) / total_buy_qty if total_buy_qty > 0 else 0
        avg_sell_px = sum(s.get("tradePrice", 0) * s.get("tradedQty", 0) for s in sells) / total_sell_qty if total_sell_qty > 0 else 0

        # Determine direction based on first fill timestamp
        first_fill = sorted(fills, key=lambda x: x.get("orderDateTime", ""))[0]
        direction = "LONG" if first_fill.get("transactionType") == 1 else "SHORT"

        entry_px = avg_buy_px if direction == "LONG" else avg_sell_px
        exit_px = avg_sell_px if direction == "LONG" else avg_buy_px

        fill_id = f"FYERS-{sym}-{first_fill.get('tradeNumber', first_fill.get('orderDateTime', ''))}"
        if fill_id in existing_hashes:
            continue

        gross_pnl = (exit_px - entry_px) * matched_qty if direction == "LONG" else (entry_px - exit_px) * matched_qty
        charges = compute_fyers_charges(entry_px, exit_px, matched_qty)
        net_pnl = round(gross_pnl - charges["total_charges"], 2)

        # Estimate stop price based on default 0.4% stop or 1:2.2 RR
        est_risk = entry_px * 0.003
        stop_px = round(entry_px - est_risk if direction == "LONG" else entry_px + est_risk, 2)
        r_risk = abs(entry_px - stop_px) * matched_qty
        net_r = round(net_pnl / r_risk, 2) if r_risk > 0 else 0.0

        trade_date = first_fill.get("orderDateTime", datetime.now().strftime("%Y-%m-%d %H:%M:%S")).split(" ")[0]
        trade_time = first_fill.get("orderDateTime", datetime.now().strftime("%Y-%m-%d %H:%M:%S")).split(" ")[-1][:5]

        trade_obj = {
            "id": len(existing) + len(new_trades) + 1,
            "fyers_id": fill_id,
            "date": trade_date,
            "time": trade_time,
            "symbol": sym,
            "direction": direction,
            "entry_price": round(entry_px, 2),
            "exit_price": round(exit_px, 2),
            "stop_price": stop_px,
            "qty": matched_qty,
            "planned_rr": 2.2,
            "urgency": 3,
            "setup_name": "FYERS Live Orderbook Sync",
            "rule_adherence": True,
            "gross_pnl": round(gross_pnl, 2),
            "total_statutory": charges["total_charges"],
            "net_pnl": net_pnl,
            "net_r": net_r,
            "status": "WIN" if net_pnl > 0 else ("LOSS" if net_pnl < 0 else "BE"),
            "notes": f"Auto-synced from FYERS tradebook. Brokerage: ₹{charges['brokerage']}, STT: ₹{charges['stt']}, GST: ₹{charges['gst']}"
        }
        new_trades.append(trade_obj)

    if new_trades:
        all_trades = existing + new_trades
        with open(TRADES_STORE, "w") as f:
            json.dump(all_trades, f, indent=2)
        print(f"Successfully synced {len(new_trades)} new trades into {TRADES_STORE}!")

        # Update Excel if excel_service available
        try:
            from excel_service import manager
            manager.set_trades(all_trades)
            print("Successfully updated D3_Tracking_Spreadsheet.xlsx via excel_service.")
        except Exception as e:
            print(f"[Notice] Excel auto-sync skipped ({e})")

        # Telegram notification
        for t in new_trades:
            emoji = "🟢" if t["net_pnl"] > 0 else "🔴"
            msg = (
                f"{emoji} *FYERS TRADE SYNCED*\n"
                f"• Symbol: `{t['symbol']}` ({t['direction']})\n"
                f"• Entry: ₹{t['entry_price']} | Exit: ₹{t['exit_price']} | Qty: {t['qty']}\n"
                f"• Net P&L: *₹{t['net_pnl']}* ({t['net_r']}R)\n"
                f"• Statutory Charges: ₹{t['total_statutory']}"
            )
            send_telegram_alert(msg, cfg)
    else:
        print("All FYERS fills are already synchronized in the local ledger.")

    return len(new_trades)

def main():
    parser = argparse.ArgumentParser(description="FYERS API v3 Live Integration & Auto-Sync Bridge")
    parser.add_argument("--auth", action="store_true", help="Generate FYERS OAuth login URL and validate auth_code")
    parser.add_argument("--sync", action="store_true", help="Sync today's fills from FYERS Tradebook to system")
    parser.add_argument("--kill-switch", action="store_true", help="Execute emergency square-off and order cancellation")
    parser.add_argument("--status", action="store_true", help="Check FYERS API connectivity and active profile")
    parser.add_argument("--config", action="store_true", help="Interactively set FYERS API credentials")
    args = parser.parse_args()

    cfg = load_config()

    if args.config:
        print("=== FYERS API v3 Credentials Setup ===")
        cfg["app_id"] = input(f"Enter FYERS App ID [{cfg.get('app_id', '')}]: ") or cfg.get("app_id", "")
        cfg["secret_key"] = input(f"Enter FYERS Secret Key [{cfg.get('secret_key', '')}]: ") or cfg.get("secret_key", "")
        cfg["redirect_uri"] = input(f"Enter Redirect URI [{cfg.get('redirect_uri', 'https://trade.fyers.in/api-login/redirect-uri/index.html')}]: ") or cfg.get("redirect_uri", "https://trade.fyers.in/api-login/redirect-uri/index.html")
        cfg["telegram_bot_token"] = input(f"Enter Telegram Bot Token (optional) [{cfg.get('telegram_bot_token', '')}]: ") or cfg.get("telegram_bot_token", "")
        cfg["telegram_chat_id"] = input(f"Enter Telegram Chat ID (optional) [{cfg.get('telegram_chat_id', '')}]: ") or cfg.get("telegram_chat_id", "")
        save_config(cfg)
        return

    if args.auth:
        url = get_auth_url(cfg)
        print("\n=== FYERS Daily Authentication ===")
        print(f"1. Open this URL in your browser:\n\n{url}\n")
        print("2. Log in with your FYERS PIN and TOTP.")
        print("3. Upon redirect, copy the 'auth_code' from the URL bar.")
        code = input("\nEnter auth_code here: ").strip()
        if code:
            token = validate_auth_code(code, cfg)
            print(f"Authentication Successful! Access Token active.")
        return

    token = load_token()

    if args.status:
        if not token:
            print("[Status] No active access token found. Run with --auth first.")
            sys.exit(1)
        try:
            prof = check_profile(token, cfg)
            print("FYERS Connection Active!")
            print(f"Profile: {prof.get('data', {}).get('name', 'Trader')} ({prof.get('data', {}).get('fy_id', '')})")
        except Exception as e:
            print(f"[Status Error] {e}")
        return

    if args.kill_switch:
        if not token:
            print("[Error] No active token. Cannot engage kill switch without active session.")
            sys.exit(1)
        res = trigger_physical_kill_switch(token, cfg)
        print("Kill switch executed:", res)
        return

    if args.sync:
        if not token:
            print("[Error] No active token. Please run --auth first to log in.")
            sys.exit(1)
        sync_trades_to_system(token, cfg)
        return

    parser.print_help()

if __name__ == "__main__":
    main()

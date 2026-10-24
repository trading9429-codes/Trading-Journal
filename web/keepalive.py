import os
import time
import urllib.request
import urllib.error
import threading
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))

def is_market_hours():
    """Checks if current IST time is within NSE execution window (09:00 AM - 11:30 AM IST, Mon-Fri)."""
    now = datetime.now(IST)
    if now.weekday() >= 5:  # Saturday or Sunday
        return False
    # 09:00 AM to 11:30 AM IST
    minutes_from_midnight = now.hour * 60 + now.minute
    start_minutes = 9 * 60        # 09:00 AM IST
    end_minutes = 11 * 60 + 30    # 11:30 AM IST
    return start_minutes <= minutes_from_midnight <= end_minutes

def get_target_url():
    url = os.environ.get("RENDER_EXTERNAL_URL") or os.environ.get("APP_URL") or ""
    if url and not url.startswith("http"):
        url = "https://" + url
    return url.rstrip("/")

def run_keepalive_loop():
    """Background daemon loop that keeps Render awake during market hours."""
    print("[Keep-Alive] Initialized Market Hours Anti-Sleep Sentinel.")
    while True:
        try:
            target_url = get_target_url()
            if target_url and is_market_hours():
                ping_url = f"{target_url}/api/ping"
                req = urllib.request.Request(ping_url, headers={"User-Agent": "Trader-KeepAlive-Sentinel/1.0"})
                try:
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        if resp.status == 200:
                            print(f"[Keep-Alive] Ping successful to {ping_url} at {datetime.now(IST).strftime('%H:%M:%S IST')}")
                except Exception as pe:
                    print(f"[Keep-Alive] Notice on ping: {pe}")
            time.sleep(600)  # Check and ping every 10 minutes
        except Exception as e:
            time.sleep(600)

def start_keepalive_daemon():
    """Starts the sentinel daemon thread if running in cloud production."""
    t = threading.Thread(target=run_keepalive_loop, daemon=True)
    t.start()

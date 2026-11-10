import http.server
import socketserver
import json
import os
import urllib.parse
from excel_service import manager, XLSX_PATH

PORT = int(os.environ.get("PORT", 8080))
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")
SETUPS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "setups_store.json")
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_store.json")
ALERTS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chartink_alerts.json")

DEFAULT_GUARDRAILS = {
    "maxDailyTrades": 2,
    "maxDailyLoss": 10000,
    "maxTradeRisk": 2500,
    "enforceTimeFilter": True
}

def get_chartink_alerts():
    if os.path.exists(ALERTS_PATH):
        try:
            with open(ALERTS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except Exception as e:
            print(f"[Chartink Alerts Read Error] {e}")
    return []

def save_chartink_alerts(alerts):
    try:
        with open(ALERTS_PATH, "w", encoding="utf-8") as f:
            json.dump(alerts[:100], f, indent=2)
        return True
    except Exception as e:
        print(f"[Chartink Alerts Save Error] {e}")
        return False

def add_chartink_alerts(new_alerts):
    current = get_chartink_alerts()
    # Prepend new alerts so newest appears first
    combined = new_alerts + current
    save_chartink_alerts(combined)
    return combined

def clear_chartink_alerts():
    save_chartink_alerts([])
    return []

def get_stock_leaderboard():
    alerts = get_chartink_alerts()
    stocks = {}
    for a in alerts:
        sym = (a.get("symbol") or "").strip().upper()
        if not sym:
            continue
        if sym not in stocks:
            stocks[sym] = {
                "symbol": sym,
                "count": 0,
                "latest_price": a.get("price", 0.0),
                "earliest_price": a.get("price", 0.0),
                "highest_price": a.get("price", 0.0),
                "lowest_price": a.get("price", 0.0),
                "latest_time": a.get("time", ""),
                "earliest_time": a.get("time", ""),
                "latest_received_at": a.get("received_at", ""),
                "setups": {},
                "categories": [],
                "color": a.get("color", "emerald"),
                "alerts": []
            }
        item = stocks[sym]
        item["count"] += 1
        item["alerts"].append(a)

        px = float(a.get("price") or 0.0)
        if px > 0:
            if item["highest_price"] == 0 or px > item["highest_price"]:
                item["highest_price"] = px
            if item["lowest_price"] == 0 or px < item["lowest_price"]:
                item["lowest_price"] = px
            item["earliest_price"] = px
            if item["count"] == 1:
                item["latest_price"] = px

        setup = a.get("setup", "Chartink Alert")
        item["setups"][setup] = item["setups"].get(setup, 0) + 1
        cat = a.get("setupCategory", "vwap")
        if cat not in item["categories"]:
            item["categories"].append(cat)

        if "megarunner" in item["categories"]:
            item["color"] = "amber"
        elif "fno" in item["categories"]:
            item["color"] = "cyan"
        elif "vwap" in item["categories"]:
            item["color"] = "emerald"
        elif "pullback" in item["categories"]:
            item["color"] = "purple"

    leaderboard = list(stocks.values())
    leaderboard.sort(key=lambda x: (x["count"], x.get("latest_received_at", "")), reverse=True)
    return leaderboard

def parse_chartink_webhook(payload, raw_body=""):
    import datetime
    
    # If payload is empty dict, try parsing raw_body as query string / urlencoded
    if not payload and raw_body:
        try:
            qs = urllib.parse.parse_qs(raw_body)
            payload = {k: v[0] if len(v) == 1 else v for k, v in qs.items()}
        except Exception:
            payload = {}

    scan_name = payload.get("scan_name") or payload.get("scanName") or payload.get("setup") or payload.get("name") or "Chartink A+ Alert"
    scan_url = payload.get("scan_url") or payload.get("scanUrl") or payload.get("url") or ""
    triggered_at = payload.get("triggered_at") or payload.get("triggeredAt") or payload.get("time") or ""

    now = datetime.datetime.now()
    if not triggered_at:
        triggered_at = now.strftime("%I:%M %p")

    # Extract stocks list (supports comma-separated string or array)
    raw_stocks = payload.get("stocks") or payload.get("stock") or payload.get("symbols") or payload.get("symbol") or ""
    if isinstance(raw_stocks, list):
        stocks_list = [str(s).strip().upper() for s in raw_stocks if str(s).strip()]
    elif isinstance(raw_stocks, str):
        stocks_list = [s.strip().upper() for s in raw_stocks.split(",") if s.strip()]
    else:
        stocks_list = []

    # Extract trigger prices
    raw_prices = payload.get("trigger_prices") or payload.get("triggerPrices") or payload.get("prices") or payload.get("price") or ""
    prices_list = []
    if isinstance(raw_prices, list):
        for p in raw_prices:
            try:
                prices_list.append(float(p))
            except Exception:
                prices_list.append(0.0)
    elif isinstance(raw_prices, (int, float)):
        prices_list = [float(raw_prices)]
    elif isinstance(raw_prices, str):
        for p in raw_prices.split(","):
            try:
                prices_list.append(float(p.strip()))
            except Exception:
                prices_list.append(0.0)

    # Determine setup category & highlight color from scan name
    scan_lower = scan_name.lower()
    if "mega" in scan_lower or "20-day" in scan_lower or "breakout" in scan_lower and "20" in scan_lower:
        color = "amber"
        category = "megarunner"
    elif "f&o" in scan_lower or "fno" in scan_lower or "future" in scan_lower:
        color = "cyan"
        category = "fno"
    elif "pullback" in scan_lower or "reversal" in scan_lower or "dip" in scan_lower:
        color = "purple"
        category = "pullback"
    else:
        color = "emerald"
        category = "vwap"

    alerts = []
    timestamp_ms = int(datetime.datetime.now().timestamp() * 1000)

    for i, sym in enumerate(stocks_list):
        px = prices_list[i] if i < len(prices_list) else 0.0
        alert_id = f"CHK-{timestamp_ms}-{i+1}"
        alerts.append({
            "id": alert_id,
            "symbol": sym,
            "price": px,
            "setup": scan_name,
            "setupCategory": category,
            "color": color,
            "time": triggered_at,
            "received_at": now.isoformat(),
            "scan_url": scan_url,
            "source": "Chartink Webhook"
        })

    return alerts

def get_guardrails():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return {**DEFAULT_GUARDRAILS, **data}
        except Exception:
            pass
    return dict(DEFAULT_GUARDRAILS)

def save_guardrails(cfg):
    try:
        current = get_guardrails()
        current.update(cfg)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(current, f, indent=2)
        return True
    except Exception as e:
        print(f"[Guardrails Save Error] {e}")
        return False

DEFAULT_SETUPS = [
    {"id": "setup-playbook-a", "name": "Setup A: VWAP & EMA Breakout (VWAP BO)", "desc": "Consolidates above 20 & 50 EMA near VWAP; 5m breakout candle with Vol >= 3x prev bar, 10 EMA > 20 EMA > 50 EMA stack. Hard stop below 20 EMA or breakout candle low. Min 1:2 R:R.", "target_rr": 2.0},
    {"id": "setup-playbook-b", "name": "Setup B: 5-Minute Volume Surge & EMA Continuation", "desc": "Scanner Vol >= 5x 20-SMA, ADR >= 4%, price well above rising 50 EMA. Never chase spike; wait for mean-reversion pull to 10/20 EMA. Bullish rejection wick. Stop below 50 EMA/swing low. Risk capped at ₹2,500.", "target_rr": 2.5},
    {"id": "setup-playbook-c", "name": "Setup C: The EMA & VWAP Pullback Reversal", "desc": "Price surges, then pulls back to rising 10/20 EMA or VWAP on low volume. Rejection wick or inside bar breakout confirming 20 EMA support. Stop below 50 EMA/pullback low. Max 2 trades/day.", "target_rr": 2.0},
    {"id": "setup-default", "name": "Default Setup", "desc": "Standard unassigned setup / system fallback", "target_rr": 2.5},
    {"id": "setup-1m-pullback", "name": "1m Pullback to 9EMA", "desc": "Trend continuation on 9EMA pullback with volume contraction", "target_rr": 2.2},
    {"id": "setup-1m-vwap", "name": "1m VWAP Bounce", "desc": "Institutional liquidity rejection at VWAP", "target_rr": 2.5},
    {"id": "setup-orb", "name": "Opening Range Breakout (ORB)", "desc": "Break of 09:15-09:30 range high/low with volume expansion", "target_rr": 2.5}
]

def get_setups():
    if os.path.exists(SETUPS_PATH):
        try:
            with open(SETUPS_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return data
        except Exception:
            pass
    return DEFAULT_SETUPS

def save_setups(setups_list):
    try:
        with open(SETUPS_PATH, "w", encoding="utf-8") as f:
            json.dump(setups_list, f, indent=2)
        return True
    except Exception as e:
        print(f"[Setups Save Error] {e}")
        return False

class WebAppHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        if path in ["/lite", "/lite/", "/minimal", "/modern"]:
            lite_path = os.path.join(PUBLIC_DIR, "lite.html")
            if os.path.exists(lite_path):
                with open(lite_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            else:
                self.send_error(404, "Lite Journal not found.")
                return
        elif path == "/api/trades":
            trades = manager.get_trades()
            stats = manager.get_stats()
            self._send_json({"trades": trades, "stats": stats})
        elif path == "/api/setups":
            self._send_json({"setups": get_setups()})
        elif path == "/api/guardrails":
            self._send_json({"guardrails": get_guardrails()})
        elif path in ("/api/scanner/alerts", "/api/webhook/chartink", "/api/chartink/alerts", "/api/scanner/leaderboard"):
            alerts = get_chartink_alerts()
            leaderboard = get_stock_leaderboard()
            self._send_json({
                "status": "ok",
                "alerts": alerts,
                "leaderboard": leaderboard,
                "count": len(alerts),
                "unique_stocks_count": len(leaderboard)
            })
        elif path == "/api/download":
            if os.path.exists(XLSX_PATH):
                with open(XLSX_PATH, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                self.send_header("Content-Disposition", 'attachment; filename="D3_Tracking_Spreadsheet.xlsx"')
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "Spreadsheet file not found.")
        elif path == "/api/sample-csv":
            sample_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "deliverables", "sample_trades_import.csv")
            if os.path.exists(sample_path):
                with open(sample_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/csv")
                self.send_header("Content-Disposition", 'attachment; filename="sample_trades_import.csv"')
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            else:
                self.send_error(404, "Sample CSV not found.")
        elif path == "/api/backup/status":
            try:
                from github_sync import get_backup_status
                self._send_json(get_backup_status())
            except Exception as e:
                self._send_json({"configured": False, "status": "Error", "last_error": str(e)})
        elif path == "/api/ping" or path == "/healthz":
            from datetime import datetime, timezone, timedelta
            ist = timezone(timedelta(hours=5, minutes=30))
            now_ist = datetime.now(ist)
            is_weekday = now_ist.weekday() < 5
            minutes = now_ist.hour * 60 + now_ist.minute
            is_market_hours = is_weekday and (9 * 60 <= minutes <= 11 * 60 + 30)
            self._send_json({
                "status": "healthy",
                "time_ist": now_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
                "market_hours": is_market_hours,
                "keepalive": "active"
            })
        elif path == "/api/scanner/alerts":
            try:
                from scanner_service import scanner_manager
                self._send_json(scanner_manager.get_scanner_data())
            except Exception as e:
                self._send_json({"error": str(e), "alerts": [], "top_stocks": []}, status=500)
        elif path == "/api/impulses":
            try:
                from impulse_service import impulse_manager
                self._send_json({"impulses": impulse_manager.get_impulses(), "stats": impulse_manager.get_stats()})
            except Exception as e:
                self._send_json({"error": str(e), "impulses": [], "stats": {}}, status=500)
        else:
            # Serve static files from PUBLIC_DIR
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"
        
        try:
            payload = json.loads(body) if body else {}
        except Exception:
            payload = {}
            
        if path == "/api/trades":
            if not payload.get("symbol") or not payload.get("entry_price") or not payload.get("stop_price"):
                self._send_json({"error": "Missing required fields (symbol, entry_price, stop_price)"}, status=400)
                return
            new_trade = manager.add_trade(payload)
            stats = manager.get_stats()
            self._send_json({"trade": new_trade, "stats": stats, "message": "Trade logged and Excel spreadsheet synchronized!"})
        elif path == "/api/trades/bulk":
            if isinstance(payload, list):
                try:
                    result = manager.set_trades(payload)
                    self._send_json(result)
                except Exception as e:
                    print(f"[Bulk Sync Error] {e}")
                    self._send_json({"status": "partial", "error": str(e), "message": "Saved locally in browser"}, status=200)
            else:
                self._send_json({"error": "Payload must be a list of trades"}, status=400)
        elif path == "/api/reset":
            result = manager.reset_examples()
            self._send_json(result)
        elif path == "/api/defaults":
            result = manager.reload_defaults()
            self._send_json(result)
        elif path == "/api/setups":
            if isinstance(payload, list):
                setups_data = payload
            else:
                setups_data = payload.get("setups", [])
            save_setups(setups_data)
            self._send_json({"status": "ok", "setups": get_setups()})
        elif path == "/api/guardrails":
            if isinstance(payload, dict):
                save_guardrails(payload)
                self._send_json({"status": "ok", "guardrails": get_guardrails()})
            else:
                self._send_json({"error": "Payload must be a json object"}, status=400)
        elif path in ("/api/webhook/chartink", "/api/chartink/webhook", "/new-stocks"):
            new_alerts = parse_chartink_webhook(payload, body)
            if new_alerts:
                add_chartink_alerts(new_alerts)
            try:
                from scanner_service import scanner_manager
                scanner_manager.process_webhook(payload)
            except Exception:
                pass
            self._send_json({
                "status": "ok",
                "received_count": len(new_alerts),
                "alerts": new_alerts,
                "message": f"Successfully processed {len(new_alerts)} Chartink webhook alert(s)!"
            })
        elif path == "/api/scanner/alerts/clear":
            clear_chartink_alerts()
            self._send_json({"status": "ok", "alerts": [], "message": "All Chartink alerts cleared"})
        elif path == "/api/scanner/test-alert":
            test_payload = payload if payload else {
                "stocks": "TRENT,DIXON",
                "trigger_prices": "7120.0,14850.0",
                "triggered_at": "09:35 AM",
                "scan_name": "Setup 4: 20-Day Range Breakout Mega-Runner"
            }
            new_alerts = parse_chartink_webhook(test_payload, body)
            if new_alerts:
                add_chartink_alerts(new_alerts)
            self._send_json({
                "status": "ok",
                "received_count": len(new_alerts),
                "alerts": new_alerts,
                "message": f"Test alert successfully delivered ({len(new_alerts)} stocks)!"
            })
        elif path == "/api/fyers/upload":
            try:
                import base64
                from fyers_parser import parse_fyers_payload
                file_content = payload.get("file_content", "")
                file_name = payload.get("file_name", "")
                base64_data = payload.get("base64", "")
                default_setup = payload.get("default_setup", "Default Setup")
                auto_commit = payload.get("auto_commit", False)

                existing_trades = manager.get_trades()
                existing_count = len(existing_trades)

                if base64_data:
                    raw_bytes = base64.b64decode(base64_data)
                    trades = parse_fyers_payload(raw_bytes, file_name=file_name, existing_count=existing_count, default_setup=default_setup)
                else:
                    trades = parse_fyers_payload(file_content, file_name=file_name, existing_count=existing_count, default_setup=default_setup)

                if auto_commit and trades:
                    combined = list(existing_trades) + list(trades)
                    manager.set_trades(combined)
                    stats = manager.get_stats()
                    self._send_json({
                        "status": "ok",
                        "trades": combined,
                        "new_trades": trades,
                        "added_count": len(trades),
                        "stats": stats,
                        "message": f"Successfully imported and synced {len(trades)} trades to Excel spreadsheet with 0.8% planned SL, 2.0% planned Target, and default setup '{default_setup}'!"
                    })
                else:
                    self._send_json({
                        "status": "ok",
                        "trades": trades,
                        "count": len(trades),
                        "message": f"Parsed {len(trades)} FYERS round-trip execution pairs."
                    })
            except Exception as e:
                import traceback
                traceback.print_exc()
                self._send_json({"error": str(e)}, status=500)
        elif path == "/api/fyers/sync":
            app_id = payload.get("app_id", "")
            access_token = payload.get("access_token", "")
            if not app_id or not access_token:
                self._send_json({"error": "Missing app_id or access_token"}, status=400)
                return
            try:
                from fyers_bridge import sync_trades_to_system, load_config
                cfg = load_config()
                cfg["app_id"] = app_id
                count = sync_trades_to_system(access_token, cfg)
                trades = manager.get_trades()
                stats = manager.get_stats()
                self._send_json({"synced_count": count, "trades": trades, "stats": stats, "message": f"Successfully synced {count} FYERS fills!"})
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
        elif path == "/api/fyers/kill-switch":
            app_id = payload.get("app_id", "")
            access_token = payload.get("access_token", "")
            if not app_id or not access_token:
                self._send_json({"error": "Missing app_id or access_token"}, status=400)
                return
            try:
                from fyers_bridge import trigger_physical_kill_switch, load_config
                cfg = load_config()
                cfg["app_id"] = app_id
                res = trigger_physical_kill_switch(access_token, cfg)
                self._send_json({"result": res, "message": "Emergency FYERS Kill Switch executed!"})
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
        elif path == "/api/backup/sync":
            try:
                from github_sync import push_trades_to_github, get_backup_status
                success, msg = push_trades_to_github(manager.get_trades(), commit_message="Manual cloud backup from Dashboard")
                status = get_backup_status()
                self._send_json({"success": success, "message": msg, "backup_status": status})
            except Exception as e:
                self._send_json({"success": False, "error": str(e)}, status=500)
        elif path == "/api/scanner/clear":
            try:
                from scanner_service import scanner_manager
                res = scanner_manager.clear_data()
                self._send_json(res)
            except Exception as e:
                self._send_json({"status": "error", "message": str(e)}, status=500)
        elif path == "/api/impulses":
            try:
                from impulse_service import impulse_manager
                new_imp = impulse_manager.add_impulse(payload)
                stats = impulse_manager.get_stats()
                self._send_json({"impulse": new_imp, "stats": stats, "message": "Impulse trade resisted and logged to Sandbox! +50 Discipline XP awarded."})
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
        elif path == "/api/impulses/clear":
            try:
                from impulse_service import impulse_manager
                res = impulse_manager.clear_impulses()
                self._send_json(res)
            except Exception as e:
                self._send_json({"error": str(e)}, status=500)
        elif path == "/api/ai/autopsy":
            try:
                from ai_service import ai_service
                trade_data = payload.get("trade", {})
                api_key = payload.get("api_key")
                provider = payload.get("provider", "gemini")
                res = ai_service.generate_trade_autopsy(trade_data, custom_api_key=api_key, provider=provider)
                self._send_json(res)
            except Exception as e:
                self._send_json({"error": str(e), "analysis": f"Autopsy error: {e}"}, status=500)
        elif path == "/api/ai/session-debrief":
            try:
                from ai_service import ai_service
                session_date = payload.get("date", "ALL")
                trades = payload.get("trades") or manager.get_trades()
                api_key = payload.get("api_key")
                provider = payload.get("provider", "gemini")
                res = ai_service.generate_session_debrief(session_date, trades, custom_api_key=api_key, provider=provider)
                self._send_json(res)
            except Exception as e:
                self._send_json({"error": str(e), "debrief": f"Debrief error: {e}"}, status=500)
        elif path == "/api/ai/chat":
            try:
                from ai_service import ai_service
                message = payload.get("message", "")
                history = payload.get("history", [])
                trades_context = payload.get("trades") or manager.get_trades()
                api_key = payload.get("api_key")
                provider = payload.get("provider", "gemini")
                res = ai_service.chat_with_coach(message, history, trades_context, custom_api_key=api_key, provider=provider)
                self._send_json(res)
            except Exception as e:
                self._send_json({"error": str(e), "reply": f"⚠️ Desk Risk Engine notice: {e}"}, status=500)
        else:
            self.send_error(404, "Endpoint not found.")

    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    active_port = PORT
    for candidate_port in [PORT, 8081, 8000]:
        try:
            httpd = socketserver.TCPServer(("", candidate_port), WebAppHandler)
            active_port = candidate_port
            break
        except OSError:
            continue
    else:
        print("Could not bind to any candidate port.")
        return

    with httpd:
        print(f"Server started on http://127.0.0.1:{active_port}")
        print(f"Data source: {XLSX_PATH}")
        try:
            from keepalive import start_keepalive_daemon
            start_keepalive_daemon()
        except Exception as e:
            print(f"[Keep-Alive] Daemon startup notice: {e}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down server.")

if __name__ == "__main__":
    run_server()

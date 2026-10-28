import http.server
import socketserver
import json
import os
import urllib.parse
from excel_service import manager, XLSX_PATH

PORT = int(os.environ.get("PORT", 8080))
PUBLIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public")

class WebAppHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        if path == "/api/trades":
            trades = manager.get_trades()
            stats = manager.get_stats()
            self._send_json({"trades": trades, "stats": stats})
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
        elif path == "/new-stocks" or path == "/api/webhook/chartink":
            try:
                from scanner_service import scanner_manager
                res = scanner_manager.process_webhook(payload)
                self._send_json(res)
            except Exception as e:
                self._send_json({"status": "error", "message": str(e)}, status=500)
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

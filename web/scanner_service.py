import os
import json
import threading
from datetime import datetime, timezone, timedelta

IST = timezone(timedelta(hours=5, minutes=30))
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
SCANNER_STORE_PATH = os.environ.get("SCANNER_STORE_PATH", os.path.join(DATA_DIR, "scanner_alerts.json"))

class ChartinkScannerManager:
    def __init__(self):
        self._lock = threading.Lock()
        self.alerts = []
        self.stock_stats = {}
        self._load_data()

    def _load_data(self):
        if os.path.exists(SCANNER_STORE_PATH):
            try:
                with open(SCANNER_STORE_PATH, "r") as f:
                    data = json.load(f)
                    self.alerts = data.get("alerts", [])
                    self.stock_stats = data.get("stock_stats", {})
                    return
            except Exception as e:
                print(f"[Scanner] Notice: could not load stored alerts: {e}")
        self.alerts = []
        self.stock_stats = {}

    def _save_data(self):
        try:
            with open(SCANNER_STORE_PATH, "w") as f:
                json.dump({
                    "alerts": self.alerts[:300],  # keep last 300 alerts
                    "stock_stats": self.stock_stats
                }, f, indent=2)
        except Exception as e:
            print(f"[Scanner] Notice: could not save alerts: {e}")

    def process_webhook(self, payload: dict) -> dict:
        """
        Processes inbound Chartink webhook payload:
        {
          "stocks": "SYMBOL 1, SYMBOL 2, SYMBOL 3",
          "trigger_prices": "2500.00,600.00,3400.00",
          "triggered_at": "12:23 am",
          "scan_name": "Sprut Trading - Vwap BO",
          "scan_url": "sprut-trading-vwap-bo",
          "alert_name": "Alert for Sprut Trading - Vwap BO",
          "webhook_url": "..."
        }
        """
        with self._lock:
            now_ist = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S IST")
            stocks_raw = str(payload.get("stocks") or "")
            prices_raw = str(payload.get("trigger_prices") or "")
            triggered_at = str(payload.get("triggered_at") or datetime.now(IST).strftime("%I:%M %p"))
            scan_name = str(payload.get("scan_name") or "1-Min Chartink Momentum")
            scan_url = str(payload.get("scan_url") or "")
            alert_name = str(payload.get("alert_name") or scan_name)

            # Split comma-separated stocks
            stock_list = [s.strip().upper().replace("NSE:", "") for s in stocks_raw.split(",") if s.strip()]
            
            # Split comma-separated trigger prices
            price_list = []
            for p in prices_raw.split(","):
                p_clean = p.strip().replace(",", "")
                try:
                    price_list.append(float(p_clean))
                except (ValueError, TypeError):
                    price_list.append(0.0)

            # Match stocks with prices
            matched_items = []
            for i, sym in enumerate(stock_list):
                px = price_list[i] if i < len(price_list) else 0.0

                # Update or initialize stock_stats frequency counter
                if sym not in self.stock_stats:
                    self.stock_stats[sym] = {
                        "symbol": sym,
                        "count": 1,
                        "latest_price": px,
                        "first_seen": now_ist,
                        "last_seen": now_ist,
                        "scans": [scan_name]
                    }
                else:
                    self.stock_stats[sym]["count"] += 1
                    if px > 0:
                        self.stock_stats[sym]["latest_price"] = px
                    self.stock_stats[sym]["last_seen"] = now_ist
                    if scan_name not in self.stock_stats[sym]["scans"]:
                        self.stock_stats[sym]["scans"].append(scan_name)

                matched_items.append({
                    "symbol": sym,
                    "price": px,
                    "count": self.stock_stats[sym]["count"]
                })

            alert_entry = {
                "id": f"ALT-{int(datetime.now().timestamp() * 1000)}",
                "received_at": now_ist,
                "triggered_at": triggered_at,
                "scan_name": scan_name,
                "scan_url": scan_url,
                "alert_name": alert_name,
                "stocks": matched_items,
                "stocks_count": len(matched_items)
            }

            self.alerts.insert(0, alert_entry)  # Newest first
            self._save_data()

            return {
                "status": "success",
                "alert": alert_entry,
                "top_stocks": self.get_top_stocks(10)
            }

    def get_top_stocks(self, limit=10):
        """Returns stocks sorted descending by alert frequency count."""
        sorted_stocks = sorted(self.stock_stats.values(), key=lambda x: x["count"], reverse=True)
        return sorted_stocks[:limit]

    def get_scanner_data(self):
        with self._lock:
            return {
                "total_alerts": len(self.alerts),
                "unique_stocks_count": len(self.stock_stats),
                "top_stocks": self.get_top_stocks(12),
                "alerts": self.alerts[:100]  # return latest 100 alerts
            }

    def clear_data(self):
        with self._lock:
            self.alerts = []
            self.stock_stats = {}
            self._save_data()
            return {"status": "success", "message": "Scanner feed and stock frequency counters reset."}

scanner_manager = ChartinkScannerManager()

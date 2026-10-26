import os
import json
from datetime import datetime, timezone, timedelta

IMPULSE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "impulses_store.json")

def get_ist_now():
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist)

class ImpulseManager:
    def __init__(self, filepath=IMPULSE_FILE):
        self.filepath = filepath
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                json.dump([], f, indent=2)

    def get_impulses(self):
        self._ensure_file()
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except Exception:
            return []

    def add_impulse(self, payload):
        impulses = self.get_impulses()
        now_ist = get_ist_now()
        
        imp_id = f"IMP-{len(impulses) + 1:03d}"
        date_str = payload.get("date") or now_ist.strftime("%Y-%m-%d")
        time_str = payload.get("time") or now_ist.strftime("%H:%M")
        
        # Default risk saved: 1R = Rs. 5,000 or custom risk amount
        saved_risk = float(payload.get("saved_risk") or 5000.0)
        
        impulse = {
            "id": imp_id,
            "date": date_str,
            "time": time_str,
            "symbol": (payload.get("symbol") or "UNKNOWN").upper().strip(),
            "trigger_price": float(payload.get("trigger_price") or 0.0),
            "direction": payload.get("direction") or "Long",
            "urge_reason": payload.get("urge_reason") or "Boredom / Lack of Stimulation",
            "notes": payload.get("notes") or "Impulse resisted and redirected to sandbox.",
            "saved_risk": saved_risk,
            "status": "Resisted & Capital Protected",
            "xp_awarded": 50
        }
        
        impulses.append(impulse)
        with open(self.filepath, "w") as f:
            json.dump(impulses, f, indent=2)
        return impulse

    def clear_impulses(self):
        with open(self.filepath, "w") as f:
            json.dump([], f, indent=2)
        return {"status": "success", "message": "All impulse logs cleared."}

    def get_stats(self):
        impulses = self.get_impulses()
        total_resisted = len(impulses)
        total_saved = sum(float(i.get("saved_risk") or 5000.0) for i in impulses)
        
        reason_counts = {}
        for imp in impulses:
            r = imp.get("urge_reason", "Other")
            reason_counts[r] = reason_counts.get(r, 0) + 1
            
        return {
            "total_resisted": total_resisted,
            "total_capital_saved": total_saved,
            "reason_breakdown": reason_counts,
            "xp_earned": total_resisted * 50
        }

impulse_manager = ImpulseManager()

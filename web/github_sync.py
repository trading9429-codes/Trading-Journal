import os
import json
import base64
import urllib.request
import urllib.error
import threading
from datetime import datetime

# GitHub Backup Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_BACKUP_TOKEN") or ""
GITHUB_REPO = os.environ.get("GITHUB_REPO", "trading9429-codes/Trading-Journal")
GITHUB_BRANCH = os.environ.get("GITHUB_BRANCH", "main")
TARGET_FILE_PATH = "web/trades_store.json"

_backup_status = {
    "configured": bool(GITHUB_TOKEN),
    "repo": GITHUB_REPO,
    "branch": GITHUB_BRANCH,
    "last_sync": None,
    "status": "Ready" if GITHUB_TOKEN else "Missing GITHUB_TOKEN environment variable",
    "last_error": None
}

def get_backup_status():
    _backup_status["configured"] = bool(os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_BACKUP_TOKEN") or GITHUB_TOKEN)
    return dict(_backup_status)

def _get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Trader-Reset-System-AutoBackup",
        "Content-Type": "application/json"
    }

def get_remote_file_info(token=None):
    """Fetches the current blob sha and content from GitHub repo."""
    tk = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_BACKUP_TOKEN") or GITHUB_TOKEN
    if not tk:
        return None, None, "No GITHUB_TOKEN configured"
        
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{TARGET_FILE_PATH}?ref={GITHUB_BRANCH}"
    req = urllib.request.Request(url, headers=_get_headers(tk), method="GET")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sha = data.get("sha")
            raw_content = base64.b64decode(data.get("content", "")).decode("utf-8")
            return sha, json.loads(raw_content), None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, None, "File not found on remote (new file)"
        err_msg = f"HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}"
        return None, None, err_msg
    except Exception as e:
        return None, None, str(e)

def push_trades_to_github(trades_list, commit_message=None):
    """Pushes the current trades list to GitHub repo."""
    tk = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_BACKUP_TOKEN") or GITHUB_TOKEN
    if not tk:
        _backup_status["status"] = "Skipped (no token)"
        _backup_status["last_error"] = "GITHUB_TOKEN not set in environment"
        return False, "GITHUB_TOKEN not set"

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = commit_message or f"Auto-backup: Synchronized trade ledger ({len(trades_list)} trades) at {now_str}"

    # 1. Fetch current sha
    sha, _, _ = get_remote_file_info(tk)

    # 2. Prepare payload
    json_bytes = json.dumps(trades_list, indent=2).encode("utf-8")
    b64_content = base64.b64encode(json_bytes).decode("utf-8")

    payload = {
        "message": msg,
        "content": b64_content,
        "branch": GITHUB_BRANCH
    }
    if sha:
        payload["sha"] = sha

    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{TARGET_FILE_PATH}"
    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=req_data, headers=_get_headers(tk), method="PUT")

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            _backup_status["last_sync"] = now_str
            _backup_status["status"] = f"Success ({len(trades_list)} trades backed up)"
            _backup_status["last_error"] = None
            return True, f"Successfully backed up {len(trades_list)} trades to GitHub."
    except urllib.error.HTTPError as e:
        err_text = e.read().decode('utf-8', errors='ignore')
        _backup_status["last_error"] = f"HTTP {e.code}: {err_text}"
        _backup_status["status"] = "Sync Failed"
        return False, _backup_status["last_error"]
    except Exception as e:
        _backup_status["last_error"] = str(e)
        _backup_status["status"] = "Sync Failed"
        return False, str(e)

def async_push_trades(trades_list, commit_message=None):
    """Triggers background push so HTTP responses are not blocked."""
    tk = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_BACKUP_TOKEN") or GITHUB_TOKEN
    if not tk:
        return
    t = threading.Thread(target=push_trades_to_github, args=(list(trades_list), commit_message), daemon=True)
    t.start()

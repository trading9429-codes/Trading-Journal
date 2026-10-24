# FYERS API v3 Simplified Integration Guide
**Trader Execution Reset System &bull; Intraday 1-Minute Equities (NSE)**

---

## 1. Executive Summary: 3 Simplified Ways to Sync

To eliminate API friction and make syncing effortless for any trader, the system provides **3 alternative sync methods**:

| Method | Best For | Prerequisites | Friction Level |
|---|---|---|---|
| **Method 1: 1-Click UI Sync** | Daily live trading directly in browser | FYERS Access Token (valid 24h) | **Zero Terminal:** Paste token in dashboard modal, click Sync |
| **Method 2: Instant Web Paste** | Zero API setup, 100% offline | None (copy rows from FYERS Web) | **Zero Auth:** Ctrl+C from FYERS Web, Ctrl+V in dashboard |
| **Method 3: Zero-Prompt Auto-CLI** | Complete background automation | One-time credentials & TOTP key | **Zero Interaction:** Script logs in silently using pure Python TOTP |

---

## 2. Method 1: In-Dashboard 1-Click Sync (Recommended for Daily Use)

1. Open the **Command Center Dashboard** ([`Dashboard.html`](file:///home/sunny/.gemini/antigravity/scratch/trader-reset-system/deliverables/Dashboard.html)).
2. In the top action bar, click **`🔌 FYERS Live Sync`**.
3. Under the **`⚡ 1-Click UI Sync`** tab:
   * Enter your **FYERS App ID** (e.g. `XC12345-100`).
   * Paste your **Daily Access Token** (generated from [FYERS API Dashboard](https://myapi.fyers.in/)).
   * Click **`💾 Remember`** so your credentials are saved in your local browser session.
4. Click **`⚡ Sync Today's Fills Now`**:
   * Today's execution fills are fetched directly from your tradebook.
   * Buy and sell legs are paired automatically.
   * Exact FYERS statutory charges (Brokerage capped at ₹20, STT 0.025% on sell, Turnover charges, SEBI fees, Stamp duty, and 18% GST) are computed down to the paisa.
   * The trades ledger and equity curves update immediately.
5. **Emergency Square-Off:** You can also click the red **`🛑 Square Off Now`** button to trigger a broker kill switch (exits open intraday positions and cancels pending orders).

---

## 3. Method 2: Instant Web Copy-Paste / File Dropzone (Zero-Auth)

If you don't want to deal with API tokens or OAuth permissions:

1. Open **FYERS Web** ([trade.fyers.in](https://trade.fyers.in/)) in your browser.
2. Navigate to **Orderbook &rarr; Tradebook**.
3. Select your filled order rows and press <kbd>Ctrl + C</kbd>.
4. In the Dashboard, click **`🔌 FYERS Live Sync`** and switch to the **`📋 Instant Web Paste`** tab.
5. Press <kbd>Ctrl + V</kbd> to paste the raw text into the box and click **`⚡ Parse & Log Trades`**.
6. Alternatively, click **`📁 Select Exported FYERS Tradebook CSV / XLSX`** to drag and drop your downloaded tradebook.

---

## 4. Method 3: Automated Zero-Prompt Background CLI (`fyers_auto_sync.py`)

For algorithmic or hands-free execution where you want background syncing without even opening a browser or copying tokens:

### Pure Python Standard Library TOTP
The script located at `scratch/trader-reset-system/web/fyers_auto_sync.py` implements RFC 6238 TOTP in pure Python (using standard library `hashlib`, `hmac`, `struct`, `base64`) with **zero pip package dependencies**.

### Setup (One-Time Only):
Run the setup once:
```bash
python3 web/fyers_auto_sync.py
```
It prompts you once for:
* FYERS Client ID (`fy_id`)
* 4-digit PIN
* 2FA TOTP Secret Key (from your Google Authenticator setup)
* App ID and Secret Key

The credentials are saved encrypted/permission-restricted in `web/.fyers_config.json` (`0600` permissions).

### Daily Hands-Free Execution:
Run whenever you want to sync fills:
```bash
python3 web/fyers_auto_sync.py --sync
```
* Generates live 6-digit TOTP code automatically.
* Authenticates session with FYERS.
* Pulls today's tradebook fills.
* Applies statutory tax formulas.
* Updates `trades_store.json` and master Excel spreadsheet (`D3_Tracking_Spreadsheet.xlsx`).
* Dispatches Telegram/WhatsApp accountability alert.

### Emergency Kill Switch CLI:
```bash
python3 web/fyers_auto_sync.py --kill-switch
```
Cancels open orders, sends market square-off orders for all intraday positions, and broadcasts an emergency alert to your accountability channel.

---

## 5. FYERS Intraday Statutory Charge Engine Verification

Every method utilizes the exact verified FYERS NSE Intraday Equity statutory formula:

$$\text{Gross P\&L} = (\text{Exit Price} - \text{Entry Price}) \times \text{Qty}$$

$$\text{Brokerage} = \min(20, \text{Buy Turnover} \times 0.0003) + \min(20, \text{Sell Turnover} \times 0.0003)$$

$$\text{STT} = \text{Sell Turnover} \times 0.00025$$

$$\text{Exchange Turnover Fee} = \text{Total Turnover} \times 0.0000297$$

$$\text{SEBI Fee} = \text{Total Turnover} \times 0.000001 \quad (\text{₹10 per crore})$$

$$\text{Stamp Duty} = \text{Buy Turnover} \times 0.00003$$

$$\text{GST} = (\text{Brokerage} + \text{Exchange Fee} + \text{SEBI Fee}) \times 0.18$$

$$\text{Net P\&L} = \text{Gross P\&L} - (\text{Brokerage} + \text{STT} + \text{Exchange} + \text{SEBI} + \text{Stamp} + \text{GST})$$

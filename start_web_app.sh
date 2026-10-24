#!/bin/bash
# Trader Execution Reset — Web Server Launcher
cd "$(dirname "$0")/web"
echo "Starting Trader Execution Reset Web App on http://127.0.0.1:8080..."
python3 server.py

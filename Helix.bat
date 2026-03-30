@echo off
chcp 65001 >nul
title 🧬 Project Helix v4.5 (Matrix Edition)
color 0A

echo ===================================================
echo  🚀 IGNITING PROJECT HELIX COMMAND CENTER...
echo ===================================================
echo.

echo [1/3] Synchronizing Cloud Intelligence (Pulling latest reports)...
git pull origin main

echo.
echo [2/3] Booting Neural Interface (Opening Browser)...
start "" "index.html"

echo.
echo [3/3] Starting Cognitive Engine (FastAPI)...
python api.py

pause
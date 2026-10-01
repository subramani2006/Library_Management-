@echo off
echo Installing dependencies...
python -m pip install -r requirements.txt
echo.
echo Starting Library Management System...
set PYTHONPATH=.
python src\main.py
pause

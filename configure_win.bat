@echo off

@REM md ./result -Force | Out-Null
if not exist "result" mkdir "result"

python -m venv .venv
.\.venv\Scripts\activate.ps1
pip install pandas openpyxl
python main.py files result

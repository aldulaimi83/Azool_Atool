@echo off
echo Building AT_Installer executable...
python -m pip install --upgrade -r requirements.txt
python build_exe.py
pause

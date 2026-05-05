@echo off
REM Build executable with PyInstaller. Run from project root.
REM Bundles test1.xlsx, test2.xlsx, videos.txt into the .exe (they must exist in this folder).
echo Installing PyInstaller...
pip install pyinstaller
echo.
if not exist test1.xlsx echo WARNING: test1.xlsx missing - create or copy before building.
if not exist test2.xlsx echo WARNING: test2.xlsx missing - create or copy before building.
if not exist videos.txt echo WARNING: videos.txt missing - create or copy before building.
echo Building testscript.exe (with data files bundled)...
python -m PyInstaller --onefile --name testscript --console ^
  --add-data "test1.xlsx;." ^
  --add-data "test2.xlsx;." ^
  --add-data "videos.txt;." ^
  run.py
echo.
echo Done. Executable: dist\testscript.exe
echo Data files (test1.xlsx, test2.xlsx, videos.txt) are inside the exe.

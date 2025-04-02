
=== Building Your Offline Survival AI App (Windows .exe) ===

1. Make sure you have Python installed:
   https://www.python.org/downloads/

2. Install PyInstaller:
   pip install pyinstaller

3. Place these two files in the same folder:
   - survival_ai_gui.py
   - survival_guides_complete.db

4. Open a terminal (CMD or PowerShell), navigate to the folder, and run:
   pyinstaller --onefile --add-data "survival_guides_complete.db;." survival_ai_gui.py

   This tells PyInstaller to:
   - Bundle the GUI app into one .exe file
   - Include the survival_guides_complete.db in the same directory

5. After it runs, check the 'dist' folder for:
   survival_ai_gui.exe

6. You can now copy just the .exe and .db to any Windows machine (no Python needed).

NOTE:
- If you want a custom icon, add: --icon=your_icon.ico
- For Mac/Linux, replace --add-data syntax with ':' instead of ';'

Godspeed, survivor.


=== Building Your Offline Survival AI App on Mac or Linux ===

REQUIREMENTS:
- Python 3 must be installed.
- Tkinter must be installed (usually included with Python).
- Install PyInstaller with pip:

    pip install pyinstaller

=== FILES NEEDED ===
Ensure the following are in the same directory:
- survival_ai_gui.py
- survival_guides_complete.db

=== BUILD THE APP ===
Use the following PyInstaller command (note the ':' instead of ';' for --add-data):

    pyinstaller --onefile --add-data "survival_guides_complete.db:." survival_ai_gui.py

This command tells PyInstaller to:
- Bundle your script into a single executable
- Include the database so it works offline

=== AFTER BUILDING ===
Check the `dist/` folder for the output file:
- On Mac: ./dist/survival_ai_gui (you can rename it to .app or .command)
- On Linux: ./dist/survival_ai_gui

=== TO RUN ===
In terminal:

    ./survival_ai_gui

If you get a permission error, make it executable:

    chmod +x survival_ai_gui

=== NOTES ===
- GUI apps may open in a terminal unless packaged as a .app (Mac).
- Works best when run from Finder or a desktop shortcut.
- For permanent GUI-style, use tools like Platypus (Mac) or desktop file shortcuts (Linux).

Survive well.

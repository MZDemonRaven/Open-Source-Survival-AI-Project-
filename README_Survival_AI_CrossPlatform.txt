
📦 OFFLINE SURVIVAL AI — Cross-Platform Edition (Windows, Linux, macOS)

This app gives you **full offline access** to:
✅ Practical SURVIVAL GUIDES for total beginners and pros  
✅ Full American Standard Version (ASV) BIBLE  
✅ Smart search functionality that handles real questions like "how to build a fire"  
✅ Clickable Table of Contents  
✅ No internet needed. No AI. Just survival and Scripture.

---

🚀 HOW TO USE (All Platforms)

1. Launch the application for your system:
   - Windows: `Survival_AI_Windows_Offline.exe`
   - macOS: `./survival_ai_gui_with_bible_and_smart_search`
   - Linux: `./survival_ai_gui_with_bible_and_smart_search`

2. Type a search phrase and hit `Enter` or click **Search**
   Try things like:
   - how to purify water
   - wilderness shelter
   - escape and evasion
   - bible light
   - genesis 1:1

3. Browse results or use the Table of Contents

---

🛡️ ANTIVIRUS / SECURITY WARNING

Because this app was created using **PyInstaller** and is not signed with a paid developer certificate:
- Some antivirus software (especially on Windows and macOS) may flag it
- **This is a false positive**
- There is NO malware or network connection in this app

If you're blocked:
- Click "Allow anyway" or "Keep"
- Add the app as an exception if needed
- On Mac: Right-click and choose "Open" (Gatekeeper will let you run it)

---

🐧 LINUX USERS

- Make the file executable:
  ```bash
  chmod +x survival_ai_gui_with_bible_and_smart_search
  ./survival_ai_gui_with_bible_and_smart_search
  ```

- You may need `tkinter` installed for the GUI:
  ```bash
  sudo apt install python3-tk
  ```

---

🍎 MAC USERS

- Open Terminal and navigate to the app folder:
  ```bash
  cd ~/Downloads/SurvivalAI
  chmod +x survival_ai_gui_with_bible_and_smart_search
  ./survival_ai_gui_with_bible_and_smart_search
  ```

- To bypass Gatekeeper:
  - Right-click the app and choose "Open"
  - Or go to System Settings > Security > “Allow anyway”

---

🛠 WANT TO BUILD FROM SOURCE?

Make sure you have Python 3 and PyInstaller installed:

- Windows:
  ```cmd
  pip install pyinstaller
  python -m PyInstaller --onefile --add-data "survival_guides_complete.db;." survival_ai_gui_with_bible_and_smart_search.py
  ```

- Linux/macOS:
  ```bash
  pip3 install pyinstaller
  pyinstaller --onefile --add-data "survival_guides_complete.db:." survival_ai_gui_with_bible_and_smart_search.py
  ```

---

✝️ Built for faith, not fear. You are not alone.

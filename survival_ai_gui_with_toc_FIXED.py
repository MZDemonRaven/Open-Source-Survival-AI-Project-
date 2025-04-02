
import os
import sys
import sqlite3
import tkinter as tk
from tkinter import scrolledtext

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

DB_PATH = resource_path("survival_guides_complete.db")

def load_titles():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM survival_guide ORDER BY title ASC")
    results = cursor.fetchall()
    conn.close()
    return results

def search_survival_guide(term, output_widget):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, category, content FROM survival_guide
        WHERE title LIKE ? OR content LIKE ?
    """, (f'%{term}%', f'%{term}%'))
    results = cursor.fetchall()
    conn.close()

    output_widget.delete(1.0, tk.END)
    if results:
        for title, category, content in results:
            output_widget.insert(tk.END, f"Title: {title}\nCategory: {category}\n{content}\n\n")
    else:
        output_widget.insert(tk.END, "No results found.")

def show_entry_by_id(entry_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, category, content FROM survival_guide WHERE id=?", (entry_id,))
    result = cursor.fetchone()
    conn.close()

    output_area.delete(1.0, tk.END)
    if result:
        title, category, content = result
        output_area.insert(tk.END, f"Title: {title}\nCategory: {category}\n\n{content}")

def on_search(event=None):
    term = search_entry.get()
    search_survival_guide(term, output_area)

def on_select(event):
    selection = toc_listbox.curselection()
    if selection:
        index = selection[0]
        entry_id = toc_entries[index][0]
        show_entry_by_id(entry_id)

# Create GUI
root = tk.Tk()
root.title("Offline Survival AI with TOC")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.X)

search_entry = tk.Entry(frame, width=50)
search_entry.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill=tk.X)
search_entry.bind("<Return>", on_search)

search_button = tk.Button(frame, text="Search", command=on_search)
search_button.pack(side=tk.LEFT)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

toc_frame = tk.Frame(main_frame)
toc_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 5), pady=(0, 10))

toc_label = tk.Label(toc_frame, text="📘 Table of Contents", anchor="w")
toc_label.pack(fill=tk.X)

toc_listbox = tk.Listbox(toc_frame, width=40)
toc_listbox.pack(fill=tk.BOTH, expand=True)
toc_listbox.bind("<<ListboxSelect>>", on_select)

scrollbar = tk.Scrollbar(toc_frame, orient=tk.VERTICAL)
scrollbar.config(command=toc_listbox.yview)
toc_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_area = scrolledtext.ScrolledText(main_frame, width=80, height=30, wrap=tk.WORD)
output_area.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10), fill=tk.BOTH, expand=True)

toc_entries = load_titles()
for _, title in toc_entries:
    toc_listbox.insert(tk.END, title)

search_entry.focus()
root.mainloop()

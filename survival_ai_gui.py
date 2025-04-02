
import sqlite3
import tkinter as tk
from tkinter import scrolledtext

def search_survival_guide(term, output_widget):
    conn = sqlite3.connect('survival_guides_complete.db')
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

def on_search(event=None):
    term = entry.get()
    search_survival_guide(term, output_area)

# Create GUI
root = tk.Tk()
root.title("Offline Survival AI")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=(0, 10))
entry.bind("<Return>", on_search)  # Pressing Enter triggers search

search_button = tk.Button(frame, text="Search", command=on_search)
search_button.pack(side=tk.LEFT)

output_area = scrolledtext.ScrolledText(root, width=80, height=25, wrap=tk.WORD)
output_area.pack(padx=10, pady=(0, 10))

entry.focus()
root.mainloop()

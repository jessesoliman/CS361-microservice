import tkinter as tk
from tkinter import ttk, TOP
from tkinter.ttk import *

def add_url():
    url = url_entry.get()
    if url:
        url_listbox.insert(tk.END, url)
        url_entry.delete(0, tk.END)

def remove_url():
    selected = url_listbox.curselection()
    if selected:
        url_listbox.delete(selected[0])

def export_csv():
    pass

def export_json():
    pass

def export_excel():
    pass


def run_micro():
    with open('run-micro.txt', 'w', encoding="utf-8") as file:
        file.write('run')


root = tk.Tk()
root.title("Sports Stats Webscraper")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# App title
app_title = ttk.Label(frame, text="Sports Stats Webscraper", font=("Arial", 20))
app_title.grid(row=0, column=0, columnspan=2)

# URL input and add button
url_label = ttk.Label(frame, text="URL:")
url_label.grid(row=1, column=0, sticky=tk.W)

url_entry = ttk.Entry(frame, width=60)
url_entry.grid(row=1, column=1)

add_button = ttk.Button(frame, text="Add", command=add_url)
add_button.grid(row=1, column=2)

# URL listbox
url_listbox = tk.Listbox(frame, width=60, height=10)
url_listbox.grid(row=2, column=0, columnspan=2, pady=10)

# Remove button
remove_button = ttk.Button(frame, text="Remove", command=remove_url)
remove_button.grid(row=2, column=2)

# Export buttons
export_csv_button = ttk.Button(frame, text="Export CSV", command=export_csv)
export_csv_button.grid(row=3, column=0, pady=5)

export_json_button = ttk.Button(frame, text="Export JSON", command=export_json)
export_json_button.grid(row=3, column=1, pady=5)

export_excel_button = ttk.Button(frame, text="Export Excel", command=export_excel)
export_excel_button.grid(row=3, column=2, pady=5)

user_pref_button = ttk.Button(frame, text="User Preferences", command=run_micro)
user_pref_button.grid(row=4, column=1)


root.mainloop()

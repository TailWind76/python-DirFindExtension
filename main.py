import os
import tkinter as tk
from tkinter import filedialog

def search_files(directory, extension):
    matched_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matched_files.append(os.path.join(root, file))
    return matched_files

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        extension = entry_extension.get()
        if extension:
            result = search_files(directory, extension)
            listbox_files.delete(0, tk.END)
            for file in result:
                listbox_files.insert(tk.END, file)

app = tk.Tk()
app.title("File Search App")
app.geometry("500x400")

label_dir = tk.Label(app, text="Select a directory:")
label_dir.pack(pady=10)

button_browse = tk.Button(app, text="Browse", command=browse_directory)
button_browse.pack()

entry_extension = tk.Entry(app, width=20)
entry_extension.pack(pady=5)

label_extension = tk.Label(app, text="Enter file extension (e.g., '.txt', '.pdf'):")
label_extension.pack()

listbox_files = tk.Listbox(app, width=80)
listbox_files.pack(padx=10, pady=10)

app.mainloop()



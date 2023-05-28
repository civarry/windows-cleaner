import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
import json

def delete_files_in_folder(folder_path):
    file_list = os.listdir(folder_path)
    deleted_count = 0
    skipped_count = 0

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                deleted_count += 1
            except Exception as e:
                skipped_count += 1
                print(f"Skipped file: {file_name}. Reason: {str(e)}")

    return deleted_count, skipped_count

def button_click():
    folder_paths = [
        "C:/Windows/Temp",
        os.path.join("C:/Users", username.get(), "AppData/Local/Temp"),
        "C:/Windows/Prefetch"
    ]

    total_deleted = 0
    total_skipped = 0

    for folder_path in folder_paths:
        if os.path.exists(folder_path):
            deleted_count, skipped_count = delete_files_in_folder(folder_path)
            total_deleted += deleted_count
            total_skipped += skipped_count
        else:
            print(f"Folder path does not exist: {folder_path}")

    messagebox.showinfo("Operation Complete", f"Deleted {total_deleted} files. Skipped {total_skipped} files.")

    # Save username to a file for future use
    save_username(username.get())

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.resizable(False, False)

def save_username(username):
    data = {"username": username}

    with open("config.json", "w") as f:
        json.dump(data, f)

def load_username():
    try:
        with open("config.json", "r") as f:
            data = json.load(f)
            return data.get("username", "")
    except FileNotFoundError:
        return ""

root = tk.Tk()
root.title("Win Cleaner")
root.geometry("200x150")
center_window(root)

frame = ttk.Frame(root)
frame.pack(fill='both', padx=10, pady=10)

username_label = ttk.Label(frame, text="Enter username:")
username_label.pack()

username = ttk.Entry(frame)
username.pack()

# Load the username if available
username_value = load_username()
username.delete(0, "end")
username.insert(0, username_value)

button_frame = ttk.Frame(root)
button_frame.pack(expand=True)

button = ttk.Button(button_frame, text="Delete Files", command=button_click)
button.pack(pady=10, padx=10, fill='both', expand=True)

root.mainloop()

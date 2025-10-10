# By AbnormalKilll

import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os

# --- Color Scheme ---
BG_COLOR = "#2e2e2e"  # Dark background
FG_COLOR = "#ffffff"  # Light foreground
BUTTON_COLOR = "#5c5c5c"  # Button background
ACTIVE_BUTTON_COLOR = "#7a7a7a"  # Button hover color
BUTTON_FG_COLOR = "#ffffff"  # Button text color
TEXT_BG_COLOR = "#1e1e1e"  # Darker text box background
TEXT_FG_COLOR = "#d4d4d4"  # Text box text color
MENU_BG_COLOR = "#3c3c3c"
MENU_FG_COLOR = "#ffffff"

# Root window setup
root = tk.Tk()
root.title("Text Editor")
root.configure(bg=BG_COLOR)
root.geometry("500x400")

# Global state variables
current_file_path = None

# Text widget with scrollbars
text_frame = tk.Frame(root, bg=BG_COLOR)
text_frame.pack(fill=tk.BOTH, expand=1, padx=1, pady=1)

text_box = tk.Text(text_frame, wrap=tk.WORD, undo=True, maxundo=-1,
                   bg=TEXT_BG_COLOR, fg=TEXT_FG_COLOR,
                   insertbackground=FG_COLOR,
                   font=('Consolas', 12))
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(text_frame, command=text_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box.config(yscrollcommand=scrollbar.set)

# Status bar
status_bar = ttk.Label(root, text="Ready", relief=tk.SUNKEN, anchor=tk.W,
                       font=('Arial', 9), background=BG_COLOR, foreground=FG_COLOR)
status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=1, pady=(0, 1))

# Functions
def new_file():
    """Create a new file, clearing the editor."""
    global current_file_path
    text_box.delete("1.0", tk.END)
    current_file_path = None
    root.title("Text Editor - Untitled")
    status_bar.config(text="Ready")

def open_file():
    """Open a file using a file dialog."""
    global current_file_path
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt"),
                                                      ("Python Scripts", "*.py"),
                                                      ("HTML Files", "*.html"),
                                                      ("CSS Files", "*.css"),
                                                      ("JavaScript Files", "*.js")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_box.delete("1.0", tk.END)
                text_box.insert("1.0", content)
            current_file_path = file_path
            root.title(f"Text Editor - {os.path.basename(file_path)}")
            status_bar.config(text=f"Opened: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    """Save the current file. Prompts for a file path if not saved before."""
    global current_file_path
    if current_file_path:
        try:
            with open(current_file_path, "w") as file:
                file.write(text_box.get("1.0", tk.END))
            status_bar.config(text=f"Saved: {current_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")
    else:
        save_file_as()

def save_file_as():
    """Save the current file with a new file path."""
    global current_file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt"),
                                                      ("Python Scripts", "*.py"),
                                                      ("HTML Files", "*.html"),
                                                      ("CSS Files", "*.css"),
                                                      ("JavaScript Files", "*.js")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_box.get("1.0", tk.END))
            current_file_path = file_path
            root.title(f"Text Editor - {os.path.basename(file_path)}")
            status_bar.config(text=f"Saved: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def exit_editor():
    """Exit the application."""
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Menu Bar
menu_bar = tk.Menu(root, bg=MENU_BG_COLOR, fg=MENU_FG_COLOR)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0, bg=MENU_BG_COLOR, fg=MENU_FG_COLOR)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Start the application
if __name__ == "__main__":
    new_file()  # Start with an empty, untitled file
    root.mainloop()


import tkinter as tk
from tkinter import ttk
import subprocess

def on_combobox_select(event):
    selected_option = combo.get()
    if selected_option == "Receiver":
        subprocess.Popen(['python3', 'client.py'])
        root.destroy()
        #  terminate Cyber Security Tool Selector here
    elif selected_option == "Sender":
        subprocess.Popen(['python3', 'server.py'])
        root.destroy()
        #  terminate Cyber Security Tool Selector here
    elif selected_option == "Hacker":
        subprocess.Popen(['python3', 'hacker.py'])
        root.destroy()
        #  terminate Cyber Security Tool Selector here
    elif selected_option == "Digital Signature":
        subprocess.Popen(['python3', 'password_verifier.py'])
        root.destroy()
        #  terminate Cyber Security Tool Selector here


# Create the main window
root = tk.Tk()
root.title("Cyber Security Tool Selector")
screen_width = 400
screen_height = 200
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, False)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create a ComboBox for selection
combo_label = ttk.Label(frame, text="Select a tool to launch:")
combo_label.pack(fill=tk.X, padx=5, pady=5)

combo = ttk.Combobox(frame, values=["Receiver", "Sender", "Hacker","Digital Signature"])
combo.pack(fill=tk.X, padx=5, pady=5)
combo.bind("<<ComboboxSelected>>", on_combobox_select)

# Run the main event loop
root.mainloop()

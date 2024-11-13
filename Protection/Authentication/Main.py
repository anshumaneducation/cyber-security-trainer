from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import os

def Start():
    type_String = server_combobox.get()
    if type_String:  # Check if a valid option was selected
        script_name = type_String.replace(' ', '_') + ".py"  # Adjust script naming convention
        script_path = os.path.join(os.getcwd(), script_name)  # Get the full path to the script
        
        if os.path.exists(script_path):
            subprocess.Popen(['python3', script_path])  # Start the script
        else:
            messagebox.showerror("Error", f"Script {script_name} not found!")
    else:
        messagebox.showerror("Error", "Please select an authentication type")

# GUI Setup for Authentication Type Selection
root = Tk()
root.title("Choose Authentication Type")
root.geometry("400x300")

# Server Selection
Label(root, text="Select Type:").pack(pady=5)
server_combobox = ttk.Combobox(root, values=['Password-Based', 'CHAP', 'IP-Based', 'MF-Authentication'])
server_combobox.pack(pady=5)

# Start Button
start_button = Button(root, text="Start", command=Start)
start_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

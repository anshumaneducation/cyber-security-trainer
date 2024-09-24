import tkinter as tk
from tkinter import ttk
import hashlib
import subprocess

encryptor_pass = hashlib.md5(b'12345').hexdigest()
print(encryptor_pass)

decryptor_pass = hashlib.md5(b'54321').hexdigest()
print(decryptor_pass)

def check_Password():
    password=textarea.get()
    input_pass = hashlib.md5(password.encode()).hexdigest() 
    print(input_pass)
    if(input_pass==encryptor_pass):
        subprocess.Popen(['python3', 'digital-signer.py'])
        root.destroy()
    elif(input_pass==decryptor_pass):
        subprocess.Popen(['python3', 'digital-verifier.py'])
        root.destroy()
# Create the main window
root = tk.Tk()

screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Set the title of the window
title_text = "Cyber Security Trainer"
node_text = "Input Password to Enter"


# Create the title string with calculated spaces
title = f"{title_text}{'      '}{node_text}"
root.title(node_text)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

textarea = tk.Entry(frame)
textarea.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Create a button that opens the file selector
pass_button = tk.Button(frame, text="Check", command=check_Password)
pass_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)


# Run the main event loop
root.mainloop()
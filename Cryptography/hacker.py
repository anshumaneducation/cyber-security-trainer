import tkinter as tk
from tkinter import ttk
import socket

# Get the hostname of the local machine
hostname = socket.gethostname()

# Get the IP address corresponding to the hostname
ip_address = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")


# Function to update the second ComboBox based on the first ComboBox selection
def update_combo2(event):
    selected_method = combo1.get()
    if selected_method == "Symmetric Encryption":
        combo2['values'] = ("DES", "TDES","RC4")
    elif selected_method == "Asymmetric Encryption":
        combo2['values'] = ("RSA", "AES")
    elif selected_method == "Hashing":
        combo2['values'] = ("SHA-256", "MD5")
    else:
        combo2['values'] = ()

# Function to handle button click
def on_button_click():
    print("Cryptography method:", combo1.get())
    print("Algorithm:", combo2.get())
    print("Received TextArea content:", received_textarea.get("1.0", tk.END))
    print("Public Key:", public_key_entry.get())
    print("Private Key:", private_key_entry.get())

# Create the main window
root = tk.Tk()
root.title(f"Cyber Security Hacker ip={ip_address}")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Step 1: Get the encrypted messages anyhow
step_label1 = ttk.Label(frame, text="Step 1: Get the encrypted messages anyhow:")
step_label1.pack(fill=tk.X, padx=5, pady=5)

# Create a TextArea for received messages
received_label = ttk.Label(frame, text="Received messages from server in encrypted format:")
received_label.pack(fill=tk.X, padx=5, pady=5)

received_textarea = tk.Text(frame, height=10, width=40)
received_textarea.pack(fill=tk.X, padx=5, pady=5)

# Step 2: Detect the encrypting method from the encryption style
step_label2 = ttk.Label(frame, text="Step 2: Detect the encrypting method from the encryption style:")
step_label2.pack(fill=tk.X, padx=5, pady=5)

# Create the first ComboBox
combo_label1 = ttk.Label(frame, text="Choose cryptography method:")
combo_label1.pack(anchor=tk.W, padx=5, pady=5)

combo1 = ttk.Combobox(frame)
combo1['values'] = ("Symmetric Encryption", "Asymmetric Encryption", "Hashing")
combo1.pack(fill=tk.X, padx=5, pady=5)
combo1.bind("<<ComboboxSelected>>", update_combo2)

# Create the second ComboBox
combo_label2 = ttk.Label(frame, text="Choose algorithm:")
combo_label2.pack(anchor=tk.W, padx=5, pady=5)

combo2 = ttk.Combobox(frame)
combo2.pack(fill=tk.X, padx=5, pady=5)

# Step 3: Get the public and/or private key
step_label3 = ttk.Label(frame, text="Step 3: Get the public and/or private key:")
step_label3.pack(fill=tk.X, padx=5, pady=5)

# Entry box for public key
public_key_label = ttk.Label(frame, text="Public Key:")
public_key_label.pack(anchor=tk.W, padx=5, pady=5)

public_key_entry = ttk.Entry(frame)
public_key_entry.pack(fill=tk.X, padx=5, pady=5)

# Entry box for private key
private_key_label = ttk.Label(frame, text="Private Key:")
private_key_label.pack(anchor=tk.W, padx=5, pady=5)

private_key_entry = ttk.Entry(frame)
private_key_entry.pack(fill=tk.X, padx=5, pady=5)

# Step 4: Get the decrypted messages
step_label4 = ttk.Label(frame, text="Step 4: Get the decrypted messages:")
step_label4.pack(fill=tk.X, padx=5, pady=5)

# Create a Button
button = ttk.Button(frame, text="Decrypt message", command=on_button_click)
button.pack(padx=5, pady=5)

received_textarea_decrypted = tk.Text(frame, height=10, width=40)
received_textarea_decrypted.pack(fill=tk.X, padx=5, pady=5)

# Run the main event loop
root.mainloop()

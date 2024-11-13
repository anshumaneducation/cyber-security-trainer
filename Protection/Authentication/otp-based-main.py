from tkinter import *
from tkinter import messagebox
import os
import socket

# File to store credentials
CREDENTIALS_FILE = "otp_based_cach.txt"

# Function to handle login
def Login():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as f:
            lines = f.readlines()
            stored_username = lines[0].strip().split('=')[1].strip('"')
            stored_password = lines[1].strip().split('=')[1].strip('"')

        username = set_username.get()
        password = set_password.get()

        if username == stored_username and password == stored_password:
            messagebox.showinfo("Login Success", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Incorrect Username or Password")
    else:
        messagebox.showerror("Error", "No credentials found! Please set a username and password.")

# Function to set the username and password and save them to the file
def SetPassword():
    username = set_username.get()
    password = set_password.get()

    if username and password:
        with open(CREDENTIALS_FILE, 'w') as f:
            f.write(f'username="{username}"\npassword="{password}"')  # Save credentials in the desired format
        messagebox.showinfo("Password Set", "Username and Password have been saved!")
    else:
        messagebox.showerror("Error", "Please enter both username and password")

# GUI Setup for Authentication Type Selection
root = Tk()
root.title("OTP Based Authentication")
root.geometry("400x300")

# Username Label and Entry
Label(root, text="Enter Username").pack(pady=5)
set_username = Entry(root)
set_username.pack(pady=5)

# Password Label and Entry (masked)
Label(root, text="Enter Password").pack(pady=5)
set_password = Entry(root, show="*")
set_password.pack(pady=5)

# Username Label and Entry
Label(root, text="Enter IP Address").pack(pady=5)
set_username = Entry(root)
set_username.pack(pady=5)

# Get OTP on IP adress connected Button
set_password_button = Button(root, text="Get OTP", command=SetPassword)
set_password_button.pack(pady=5)

## send otp to that ip adress which will be connected using socket programming 4 digit otp sent using random digit generation

# Password Label and Entry (masked)
Label(root, text="Enter OTP").pack(pady=5)
set_password = Entry(root, show="*")
set_password.pack(pady=5)

# Set Password Button
set_password_button = Button(root, text="Set Password", command=SetPassword)
set_password_button.pack(pady=5)

# Login Button
login_button = Button(root, text="Login", command=Login)
login_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

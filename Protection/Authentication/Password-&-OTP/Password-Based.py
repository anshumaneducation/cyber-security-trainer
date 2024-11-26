from tkinter import *
from tkinter import messagebox
import os

# File to store credentials
CREDENTIALS_FILE = "password_based_cach.txt"

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
root.title("Password Based Authentication")
root.geometry("400x300")

# Username Label and Entry
Label(root, text="Enter Username").pack(pady=5)
set_username = Entry(root)
set_username.pack(pady=5)

# Password Label and Entry (masked)
Label(root, text="Enter Password").pack(pady=5)
set_password = Entry(root, show="*")
set_password.pack(pady=5)

# Login Button
login_button = Button(root, text="Login", command=Login)
login_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

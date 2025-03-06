from tkinter import *
from tkinter import messagebox
import random
import socket
import threading

# File path
file_path = "/etc/encrypted_file.enc"

# Check if the encrypted file exists before opening the app
if not os.path.exists(file_path):
    exit()

server_ip = None
port_address = 8080
client_socket = None
validate_otp=False

# File to store credentials
CREDENTIALS_FILE = "password_based_cach.txt"

# Global variables for OTP management
generated_otp = None


def send_otp_thread():
    global server_ip, generated_otp, client_socket

    server_ip = ip_entry.get()
    if not server_ip:
        messagebox.showerror("Error", "Please enter a valid IP address")
        return

    try:
        # Create a TCP client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, port_address))
        print(f"Connected to server at {server_ip}:{port_address}")

        # Generate a random 4-digit OTP
        generated_otp = str(random.randint(1000, 9999))
        print(f"Generated OTP: {generated_otp}")

        # Send the OTP to the server
        client_socket.sendall(generated_otp.encode())
        messagebox.showinfo("OTP Sent", f"OTP sent to server: {generated_otp}")
        validate_otp=False
        # Start a thread to listen for server responses
        receiver_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
        receiver_thread.start()
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect to server: {e}")


def receive_messages(sock):
    try:
        while True:
            response = sock.recv(1024).decode()
            if not response:
                print("Disconnected from server.")
                break
            print(f"Server: {response}")
    except Exception as e:
        print(f"Error receiving data: {e}")
    finally:
        sock.close()


def verify_otp():
    global generated_otp, validate_otp
    user_otp = otp_entry.get()

    if not generated_otp:
        messagebox.showerror("Error", "No OTP generated yet. Please request an OTP first.")
        return

    if user_otp == generated_otp:
        validate_otp=True
        messagebox.showinfo("OTP Success", "Welcome!")
    else:
        validate_otp=False
        messagebox.showerror("OTP Error", "Invalid OTP. Please try again.")


def set_password():
    username = username_entry.get()
    password = password_entry.get()

    if username and password and validate_otp:
        with open(CREDENTIALS_FILE, 'w') as f:
            f.write(f'username="{username}"\npassword="{password}"')  # Save credentials in the desired format
        messagebox.showinfo("Password Set", "Username and Password have been saved!")
    else:
        messagebox.showerror("Error", "Please enter both username and password also validate otp")


def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            credentials = f.read()
            if (f'username="{username}"' in credentials and f'password="{password}"' in credentials) & validate_otp:
                messagebox.showinfo("Login Successful", "You are now logged in.")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password or OTP Validation.")
    except FileNotFoundError:
        messagebox.showerror("Error", "Credentials not set. Please set them first.")

def show_username_thread():
    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            credentials = f.read()
            # Extract username from the file content
            username = credentials.split('\n')[0].split('=')[1].strip('"')
            messagebox.showinfo("Saved Username", f"Username: {username}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No credentials found. Please set them first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def show_password_thread():
    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            credentials = f.read()
            # Extract password from the file content
            password = credentials.split('\n')[1].split('=')[1].strip('"')
            messagebox.showinfo("Saved Password", f"Password: {password}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No credentials found. Please set them first.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



# GUI Setup
root = Tk()
root.title("OTP Based Authentication")
root.geometry("400x400")

# Username Label and Entry
Label(root, text="Enter Username").pack(pady=5)
username_entry = Entry(root)
username_entry.pack(pady=5)

# Password Label and Entry (masked)
Label(root, text="Enter Password").pack(pady=5)
password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

# IP Address Label and Entry
Label(root, text="Enter Server IP Address").pack(pady=5)
ip_entry = Entry(root)
ip_entry.pack(pady=5)

# Get OTP Button
otp_button = Button(root, text="Get OTP", command=send_otp_thread)
otp_button.pack(pady=5)

# OTP Label and Entry
Label(root, text="Enter OTP").pack(pady=5)
otp_entry = Entry(root)
otp_entry.pack(pady=5)

# Verify OTP Button
verify_button = Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack(pady=5)

# Set Password Button
set_password_button = Button(root, text="Set Password", command=set_password)
set_password_button.pack(pady=5)

# Login Button
login_button = Button(root, text="Login", command=login)
login_button.pack(pady=5)

show_username = Button(root,text="Show Username", command=show_username_thread )
show_username.pack(pady=5)

show_password = Button(root,text="Show Password", command=show_password_thread )
show_password.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

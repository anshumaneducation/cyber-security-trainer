import tkinter as tk
import smtplib
import subprocess
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def log_message(message):
    log_text.insert(tk.END, message + '\n')
    log_text.yview(tk.END)

# Button 1 send email
def on_button1_click():
    log_message("Button 1 clicked")
    senders_email = entry_box.get()
    # Email account credentials
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Common port for TLS
    username = 'your-email@example.com'  # Replace with your email
    password = 'your-password'  # Replace with your email password

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = senders_email
    msg['Subject'] = 'Subject: Email with Attachment'

    # Email body
    body = 'Please find the attached document.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file
    filename = 'document.pdf'  # Replace with your file
    try:
        with open(filename, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=filename)
            part['Content-Disposition'] = f'attachment; filename="{filename}"'
            msg.attach(part)
    except FileNotFoundError:
        log_message(f"Error: File {filename} not found.")
        return

    # Connect to the server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(username, password)  # Log in to your account
            server.sendmail(msg['From'], msg['To'], msg.as_string())  # Send email
        log_message('Email with attachment sent successfully!')
    except Exception as e:
        log_message(f"Error: {e}")

# Function to read subprocess output
def read_subprocess_output(process):
    for line in iter(process.stdout.readline, ''):
        log_message(line.strip())
    process.stdout.close()

def on_button2_click():
    log_message("Button 2 clicked")
    try:
        # Start the Node.js server
        process = subprocess.Popen(['node', 'server.js'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Start a thread to read subprocess output
        threading.Thread(target=read_subprocess_output, args=(process,), daemon=True).start()
        
        log_message("Node.js server started successfully.")
    except Exception as e:
        log_message(f"Error: {e}")



# GUI setup
root = tk.Tk()
root.title("Phishing Attack Setup")

# Log text widget setup
log_frame = tk.Frame(root)
log_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="NSEW")

log_text = tk.Text(log_frame, wrap='word', height=10, width=50)
log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

log_scroll = tk.Scrollbar(log_frame, orient='vertical', command=log_text.yview)
log_scroll.pack(side=tk.RIGHT, fill='y')

log_text.config(yscrollcommand=log_scroll.set)


# Create an entry box with default text
entry_box = tk.Entry(root)
entry_box.insert(0, "email@email.com")  # Set default text
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="W")

# Create two buttons
button1 = tk.Button(root, text="Send Phishing Email", command=on_button1_click)
button1.grid(row=0, column=2, padx=10, pady=10, sticky="NSEW")

button2 = tk.Button(root, text="Create Server", command=on_button2_click)
button2.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Start the GUI event loop
root.mainloop()





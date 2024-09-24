import subprocess
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, Text, Scrollbar, VERTICAL, RIGHT, Y, END

# Functions
def execute_iptables_command(command):
    """Executes the given iptables command."""
    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", "Command executed successfully!")
    except subprocess.CalledProcessError as e:
        # messagebox.showerror("Error", f"Failed to execute command: {e}")
        print(e)

def add_rule():
    rule = f"sudo iptables -A INPUT -p {protocol.get()}"

    if source_ip.get():
        rule += f" -s {source_ip.get()}"
    if source_port.get():
        rule += f" --sport {source_port.get()}"
    if destination_ip.get():
        rule += f" -d {destination_ip.get()}"
    if destination_port.get():
        rule += f" --dport {destination_port.get()}"

    rule += f" -j {rule_type.get()}"
    execute_iptables_command(rule)

def remove_rule():
    rule = f"sudo iptables -D INPUT -p {protocol.get()}"

    if source_ip.get():
        rule += f" -s {source_ip.get()}"
    if source_port.get():
        rule += f" --sport {source_port.get()}"
    if destination_ip.get():
        rule += f" -d {destination_ip.get()}"
    if destination_port.get():
        rule += f" --dport {destination_port.get()}"

    rule += f" -j {rule_type.get()}"
    execute_iptables_command(rule)

def view_rules():
    try:
        result = subprocess.run("sudo iptables -L -v", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        display_text(result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to retrieve rules: {e}")
        print(e)

def view_status():
    try:
        result = subprocess.run("sudo ufw status", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        display_text(result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to retrieve firewall status: {e}")
        print(e)

def view_logs():
    try:
        result = subprocess.run("sudo iptables -L -v", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        display_text(result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to retrieve logs: {e}")
        print(e)

def display_text(text):
    output_text.delete(1.0, END)
    output_text.insert(END, text)

# GUI setup for Firewall Management
root = Tk()
root.title("Firewall Protection Simulation")

# Variables to hold user inputs
rule_type = StringVar()
protocol = StringVar()
source_ip = StringVar()
destination_ip = StringVar()
source_port = StringVar()
destination_port = StringVar()

# GUI Components
Label(root, text="Rule Type (ACCEPT/DROP/REJECT/LOG):").pack()
Entry(root, textvariable=rule_type).pack()

Label(root, text="Protocol (tcp/udp):").pack()
Entry(root, textvariable=protocol).pack()

Label(root, text="Source IP (leave empty for any):").pack()
Entry(root, textvariable=source_ip).pack()

Label(root, text="Destination IP (leave empty for any):").pack()
Entry(root, textvariable=destination_ip).pack()

Label(root, text="Source Port (leave empty for any):").pack()
Entry(root, textvariable=source_port).pack()

Label(root, text="Destination Port (leave empty for any):").pack()
Entry(root, textvariable=destination_port).pack()

Button(root, text="Add Rule", command=add_rule).pack()
Button(root, text="Remove Rule", command=remove_rule).pack()
Button(root, text="View Rules", command=view_rules).pack()
Button(root, text="Firewall Status", command=view_status).pack()
Button(root, text="View Logs", command=view_logs).pack()

# Output Text Area with Scrollbar
output_text = Text(root, height=10, wrap="word")
output_text.pack(expand=True, fill="both")

scrollbar = Scrollbar(root, orient=VERTICAL, command=output_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

output_text.config(yscrollcommand=scrollbar.set)

# Run the GUI loop
root.mainloop()

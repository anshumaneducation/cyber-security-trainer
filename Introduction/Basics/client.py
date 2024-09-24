import socket
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
import paho.mqtt.client as mqtt

def send_tcp_message(ip, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((ip, port))
            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
        return response
    except Exception as e:
        return f"Error: {e}"

def send_udp_message(ip, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            client_socket.sendto(message.encode(), (ip, port))
            response, _ = client_socket.recvfrom(1024)
        return response.decode()
    except Exception as e:
        return f"Error: {e}"

def send_http_request(ip, port, endpoint):
    try:
        url = f"http://{ip}:{port}/{endpoint}"
        response = requests.get(url)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def send_ftp_request(ip, port, command):
    try:
        from ftplib import FTP
        ftp = FTP()
        ftp.connect(ip, port)
        ftp.login()  # login as anonymous
        response = ftp.sendcmd(command)
        ftp.quit()
        return response
    except Exception as e:
        return f"Error: {e}"

def send_mqtt_message(ip, port, topic, message):
    def on_connect(client, userdata, flags, rc):
        client.publish(topic, message)
        client.disconnect()
    
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect(ip, port)
        client.loop_forever()
        return "Message sent"
    except Exception as e:
        return f"Error: {e}"

def send_message():
    ip = ip_entry.get()
    port = int(port_entry.get())
    message = message_entry.get()
    endpoint = endpoint_entry.get()
    topic = topic_entry.get()
    
    server_type = server_combobox.get()
    result = ""
    
    if server_type == 'TCP':
        result = send_tcp_message(ip, port, message)
    elif server_type == 'UDP':
        result = send_udp_message(ip, port, message)
    elif server_type == 'HTTP':
        result = send_http_request(ip, port, endpoint)
    elif server_type == 'FTP':
        result = send_ftp_request(ip, port, message)
    elif server_type == 'MQTT':
        result = send_mqtt_message(ip, port, topic, message)
    else:
        result = "Please select a valid server type."
    
    result_text.delete("1.0", END)
    result_text.insert(END, result)

# GUI Setup
root = Tk()
root.title("Client Application")
root.geometry("500x400")

# Server Type Selection
Label(root, text="Select Server Type:").pack(pady=5)
server_combobox = ttk.Combobox(root, values=['TCP', 'UDP', 'HTTP', 'FTP', 'MQTT'])
server_combobox.pack(pady=5)

# IP Entry
Label(root, text="Server IP:").pack(pady=5)
ip_entry = Entry(root, width=30)
ip_entry.pack(pady=5)

# Port Entry
Label(root, text="Port:").pack(pady=5)
port_entry = Entry(root, width=30)
port_entry.pack(pady=5)

# Message Entry
Label(root, text="Message/Command:").pack(pady=5)
message_entry = Entry(root, width=30)
message_entry.pack(pady=5)

# HTTP Endpoint Entry
Label(root, text="HTTP Endpoint:").pack(pady=5)
endpoint_entry = Entry(root, width=30)
endpoint_entry.pack(pady=5)

# MQTT Topic Entry
Label(root, text="MQTT Topic:").pack(pady=5)
topic_entry = Entry(root, width=30)
topic_entry.pack(pady=5)

# Send Button
send_button = Button(root, text="Send Message", command=send_message)
send_button.pack(pady=5)

# Result Text
result_text = Text(root, height=10, width=60)
result_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

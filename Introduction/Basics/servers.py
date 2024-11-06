# server_gui.py
import tkinter as tk
import subprocess

def start_http():
    global http_process
    http_process = subprocess.Popen(['python3', 'http_server.py'])

def start_ftp():
    global ftp_process
    ftp_process = subprocess.Popen(['python3', 'ftp_server.py'])

def start_mqtt():
    global mqtt_process
    mqtt_process = subprocess.Popen(['python3', 'mqtt_server.py'])

def stop_servers():
    global http_process, ftp_process, mqtt_process
    http_process.terminate()
    ftp_process.terminate()
    mqtt_process.terminate()

# Create the GUI
root = tk.Tk()
root.title("Server Control")

http_button = tk.Button(root, text="Start HTTP Server", command=start_http)
http_button.pack()

ftp_button = tk.Button(root, text="Start FTP Server", command=start_ftp)
ftp_button.pack()

mqtt_button = tk.Button(root, text="Start MQTT Server", command=start_mqtt)
mqtt_button.pack()

stop_button = tk.Button(root, text="Stop All Servers", command=stop_servers)
stop_button.pack()

root.mainloop()

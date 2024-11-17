
To enable SSH on a Linux machine (such as **Device 2**), here’s a complete guide:

### **Step 1: Install the SSH Server (if not already installed)**
First, you need to make sure that the SSH server (`openssh-server`) is installed on Device 2.

```bash
sudo apt update
sudo apt install openssh-server -y
```

### **Step 2: Enable and Start the SSH Service**
After installing, enable and start the SSH service so that it runs automatically at boot.

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

To check if SSH is running correctly:

```bash
sudo systemctl status ssh
```

You should see a message saying that the SSH service is **active (running)**.

### **Step 3: Check the SSH Listening Port**
By default, SSH listens on port **22**. You can confirm this with:

```bash
sudo netstat -tuln | grep ssh
```

Make sure your firewall (if enabled) allows traffic on port 22:
```bash
sudo ufw allow 22
```

### **Step 4: Find the IP Address of Device 2**
You’ll need the IP address of Device 2 to connect to it remotely.

```bash
ip addr
```

Look for the `inet` address under the `eth0` or `wlan0` interface. For example, it might look like `192.168.1.20`.

### **Step 5: SSH from Device 1 to Device 2**
Now, on Device 1, use the `ssh` command to connect to Device 2 using its IP address, username, and password.

```bash
ssh your_username@192.168.1.20
```

It will prompt for the password. Enter the **same password** you use to log in to Device 2.

- **your_username**: The username you use to log in to Device 2.
- **192.168.1.20**: The IP address of Device 2.

### **Step 6: Setting Up Passwordless SSH (Optional)**
To avoid typing the password every time, you can set up **passwordless SSH** using SSH keys:

1. **Generate an SSH key** on Device 1:
   ```bash
   ssh-keygen -t rsa -b 4096
   ```
   Press **Enter** to accept the default file location and **leave the passphrase empty** if you want passwordless access.

2. **Copy the public key** to Device 2:
   ```bash
   ssh-copy-id your_username@192.168.1.20
   ```
   Enter your password for Device 2 when prompted.

3. Now, you can SSH into Device 2 without entering a password:
   ```bash
   ssh your_username@192.168.1.20
   ```

### **Step 7: Troubleshooting (if SSH is not working)**
- Make sure the SSH service is running:
  ```bash
  sudo systemctl restart ssh
  sudo systemctl status ssh
  ```
- Ensure that **port 22** is open in the firewall:
  ```bash
  sudo ufw allow 22
  sudo ufw enable
  ```

### **Final Notes**
- Use `ssh -v` for verbose output if you encounter issues:
  ```bash
  ssh -v your_username@192.168.1.20
  ```

- If Device 2 is behind a router, ensure port forwarding is configured if connecting over the internet.

This should get your SSH connection working smoothly so that you can remotely run your firewall scripts on Device 2!
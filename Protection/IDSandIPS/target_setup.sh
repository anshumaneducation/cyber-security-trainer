#!/bin/bash
# Target Script: Simulates a vulnerable service.

LISTEN_PORT=80  # Port to simulate a web server.

echo "Starting a simulated vulnerable service on port: $LISTEN_PORT"

# 1. Start a Simple HTTP Server
python3 -m http.server $LISTEN_PORT &

# 2. Simulate SSH Service
echo "[INFO] Simulating SSH service on port 22"
sudo apt install -y openssh-server
sudo service ssh start

# 3. Monitor for Attacks
echo "Monitoring incoming connections..."
sudo tcpdump -i eth0 -w /tmp/target_traffic.pcap &

echo "Vulnerable services are running."

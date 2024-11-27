#!/bin/bash
# Defender Script: Starts Snort in IDS or IPS mode and monitors logs.

INTERFACE="eth0"  # Replace with your network interface.
LOG_DIR="/var/log/snort"

echo "Starting Snort in IDS mode on interface: $INTERFACE"

# Ensure Snort is installed
if ! command -v snort &> /dev/null; then
    echo "Snort is not installed. Installing now..."
    sudo apt update && sudo apt install -y snort
fi

# Start Snort in IDS mode (console output and log alerts)
sudo snort -i $INTERFACE -c /etc/snort/snort.conf -A console &

# (Optional) Start Snort in IPS mode (requires iptables)
# Uncomment the following lines to enable IPS:
sudo iptables -A INPUT -j NFQUEUE --queue-num 0
sudo iptables -A OUTPUT -j NFQUEUE --queue-num 0
sudo snort -Q --daq nfq --daq-var queue=0 -c /etc/snort/snort.conf

echo "Snort is running. Monitoring logs at: $LOG_DIR"

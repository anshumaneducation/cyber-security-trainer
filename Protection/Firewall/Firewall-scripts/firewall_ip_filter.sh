# Summary of the Script's Actions:

#     Blocking Incoming Traffic from a Specific IP:
#         The script blocks any incoming traffic from the IP 192.168.1.100. You can change this IP to any address you want to block.

#     Allowing Incoming Traffic from a Trusted IP:
#         The script allows incoming traffic from the IP 192.168.1.50. You can change this IP to any address you want to trust.

# Use Cases:

#     Blocking Malicious IPs: If you know a certain IP address is sending unwanted or malicious traffic to your system, you can block it to prevent any further access.
#     Allowing Trusted IPs: If you have a specific server or trusted device (e.g., a monitoring system or internal network), you can ensure it has access to your system while blocking others.



#!/bin/bash
# Script to block or allow traffic based on IP addresses

echo "Setting up IP address filtering..."

# Block traffic from a specific IP (customize this)
BLOCKED_IP="192.168.1.100"
sudo iptables -A INPUT -s $BLOCKED_IP -j DROP
echo "Blocked IP address: $BLOCKED_IP"

# Allow traffic from a trusted IP
TRUSTED_IP="192.168.1.50"
sudo iptables -A INPUT -s $TRUSTED_IP -j ACCEPT
echo "Allowed traffic from trusted IP: $TRUSTED_IP"

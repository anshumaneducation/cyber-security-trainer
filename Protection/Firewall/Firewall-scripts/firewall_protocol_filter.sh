# Summary:

#     Allowed: TCP traffic, HTTP traffic (port 80), and UDP traffic.
#     Blocked: ICMP traffic (ping requests).

# This script now:

#     Allows essential protocols (TCP for most services, HTTP for web traffic, and UDP for applications like DNS or VoIP).
#     Blocks ping requests (ICMP) for increased security against discovery.


#!/bin/bash
# Script to filter traffic based on protocols

echo "Setting up protocol-based firewall rules..."

# Allow only TCP traffic
sudo iptables -A INPUT -p tcp -j ACCEPT

# Allow HTTP traffic (port 80)
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
echo "Allowed HTTP traffic on port 80."

# Allow UDP traffic
sudo iptables -A INPUT -p udp -j ACCEPT
echo "Allowed UDP traffic."

# Block ICMP (ping) requests
sudo iptables -A INPUT -p icmp -j DROP
echo "Blocked ICMP traffic (ping requests)."

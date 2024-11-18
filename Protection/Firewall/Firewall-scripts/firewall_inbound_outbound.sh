# Summary of What the Script Does:

#     Outbound Traffic: Allows all outgoing traffic by default.
#     Inbound Traffic:
#         Blocks all incoming traffic by default (for security).
#         Specifically allows incoming traffic on:
#             Port 22 (SSH) for remote login.
#             Port 80 (HTTP) for non-secure web traffic.
#             Port 443 (HTTPS) for secure web traffic.
#         Allows all traffic from the localhost (loopback) interface, enabling local communication within your machine.
#         Allows traffic related to established connections (e.g., responses to outgoing requests like visiting a website or an ongoing SSH session).

# Potential Use Case:

#     Security for a server where you want to ensure only certain ports (like SSH, HTTP, and HTTPS) are open for incoming connections, while blocking all others. Outgoing traffic is not restricted, meaning you can still access websites or make external requests without any problems.



#!/bin/bash
# Script to set up basic inbound and outbound firewall rules

echo "Setting up basic inbound and outbound firewall rules..."

# Allow all outgoing traffic
sudo iptables -P OUTPUT ACCEPT

# Block all incoming traffic by default
sudo iptables -P INPUT DROP

# Allow incoming traffic on specific ports (SSH, HTTP, HTTPS)
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow traffic from localhost
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow established and related connections
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

echo "Inbound and outbound rules applied."

#     Blocked SMTP traffic on port 25:
#         Blocks incoming traffic on port 25, preventing SMTP traffic (used for email sending).

#     Blocked HTTP traffic on port 80:
#         Blocks incoming HTTP traffic (typically used for web browsing over HTTP) on port 80.

#     Dropped traffic on port 8080:
#         Drops any incoming traffic on port 8080, which may be used by applications running on non-standard HTTP ports.

#     Allowed HTTPS traffic on port 443:
#         Allows incoming HTTPS traffic (secure web traffic) on port 443.

# Summary:

#     Blocked: SMTP (port 25) and HTTP (port 80).
#     Dropped: Traffic on port 8080.
#     Allowed: HTTPS (port 443).




#!/bin/bash
# Script to filter traffic based on ports

echo "Setting up port-based firewall rules..."

# Block all traffic on port 25 (SMTP)
sudo iptables -A INPUT -p tcp --dport 25 -j DROP
echo "Blocked SMTP traffic on port 25."

# Block all traffic on port 80 (HTTP)
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
echo "Blocked HTTP traffic on port 80."

# Drop traffic on port 8080
sudo iptables -A INPUT -p tcp --dport 8080 -j DROP
echo "Dropped traffic on port 8080."

# Allow traffic on a specific port (example: port 443 for HTTPS)
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
echo "Allowed HTTPS traffic on port 443."

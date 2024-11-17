#Verified:

#Testing and Troubleshooting:

   # After running this script, try opening a new website. It should be blocked.
   # Important: If you run this on a remote machine, ensure you have a way to revert the changes or access the machine via some other means (e.g., physical console or rescue mode), as this will block any new outbound connections.

   #The script allows only established or related traffic while blocking all new incoming connection attempts.
#This is a basic security measure often used to prevent unauthorized access while allowing responses to requests that your machine initiated.


#!/bin/bash
# Script to filter traffic based on connection state

echo "Setting up connection state-based rules..."

##### For servers side
# Allow only established and related incoming connections
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
echo "Allowed only established and related incoming connections."

# Block new incoming connections
sudo iptables -A INPUT -m conntrack --ctstate NEW -j DROP
echo "Blocked new incoming connections."

#### For client side

# Allow only established and related outgoing connections
sudo iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
echo "Allowed only established and related outgoing connections."

# Block new outgoing connections
sudo iptables -A OUTPUT -m conntrack --ctstate NEW -j DROP
echo "Blocked new outgoing connections."

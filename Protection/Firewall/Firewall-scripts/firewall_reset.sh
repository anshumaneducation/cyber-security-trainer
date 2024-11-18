# What Happens After Running This Script?

#     No restrictions: Your system will accept all inbound and outbound traffic because the default policies are set to ACCEPT.
#     Firewall effectively disabled: After flushing the rules and resetting the policies to ACCEPT, the firewall will no longer block any connections unless other firewall rules are manually added later.



#!/bin/bash
# Script to reset all iptables rules

echo "Resetting all iptables rules to default..."

# Flush all rules
sudo iptables -F

# Reset default policies
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

echo "All rules have been reset."

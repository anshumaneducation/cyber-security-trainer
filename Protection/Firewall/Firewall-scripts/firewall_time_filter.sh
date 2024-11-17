#     Block Incoming Traffic:
#         sudo iptables -A INPUT -m time --timestart 20:00 --timestop 06:00 --days Mon,Tue,Wed,Thu,Fri -j DROP
#         This rule blocks incoming traffic during the specified time period.

#     Block Outgoing Traffic:
#         sudo iptables -A OUTPUT -m time --timestart 20:00 --timestop 06:00 --days Mon,Tue,Wed,Thu,Fri -j DROP
#         This rule blocks outgoing traffic during the specified time period.

# Summary:

#     Blocked Incoming Traffic: Between 8 PM and 6 AM Everyday.
#     Blocked Outgoing Traffic: Between 8 PM and 6 AM Everyday.

## To see time setting `timedatectl`
#!/bin/bash
# Script to set up time-based firewall rules for India (UTC +5:30)

echo "Setting up time-based rules for India..."

# Block incoming traffic between 8 PM and 6 AM IST (which is 2:30 PM to 12:30 AM UTC)
sudo iptables -A INPUT -m time --timestart 14:30 --timestop 00:30 -j DROP
echo "Blocked incoming traffic between 8 PM and 6 AM India Time (2:30 PM to 12:30 AM UTC)."

# Block outgoing traffic between 8 PM and 6 AM IST (which is 2:30 PM to 12:30 AM UTC)
sudo iptables -A OUTPUT -m time --timestart 14:30 --timestop 00:30 -j DROP
echo "Blocked outgoing traffic between 8 PM and 6 AM India Time (2:30 PM to 12:30 AM UTC)."

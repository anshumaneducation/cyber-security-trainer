#!/bin/bash

# TCP Ping to check if a host is up on port 80 and 443
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing TCP Ping on $target for ports 80 and 443..."

# Check port 80
nc -zv -w1 $target 80 2>&1 | grep "succeeded" || echo "Port 80 is closed or host is unreachable."

# Check port 443
nc -zv -w1 $target 443 2>&1 | grep "succeeded" || echo "Port 443 is closed or host is unreachable."

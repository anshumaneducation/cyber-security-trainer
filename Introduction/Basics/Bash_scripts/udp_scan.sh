#!/bin/bash

# UDP Port Scan to check for open UDP ports
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing UDP Port Scan on $target..."
nmap -sU $target

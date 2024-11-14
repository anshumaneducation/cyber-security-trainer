#!/bin/bash

# Fast Scan to scan top 1000 ports
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing Fast Scan on $target..."
nmap -F $target

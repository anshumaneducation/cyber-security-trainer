#!/bin/bash

# Null Scan to check for open ports
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing Null Scan on $target..."
nmap -sN $target

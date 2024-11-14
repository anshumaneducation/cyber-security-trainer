#!/bin/bash

# FIN Stealth Scan to check for open ports using FIN packets
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing FIN Stealth Scan on $target..."
nmap -sF $target

#!/bin/bash

# SYN Stealth Scan to detect open ports without completing the handshake
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing SYN Stealth Scan on $target..."
nmap -sS $target

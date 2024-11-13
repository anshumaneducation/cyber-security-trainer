#!/bin/bash

# ICMP Ping to check if a host is up
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Performing ICMP Ping on $target..."
ping -c 4 $target

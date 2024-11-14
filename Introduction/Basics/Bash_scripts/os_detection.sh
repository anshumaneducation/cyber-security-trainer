#!/bin/bash

# OS Detection to try identifying the target OS
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target>"
    exit 1
fi

target=$1

echo "Detecting OS on $target..."
nmap -O $target

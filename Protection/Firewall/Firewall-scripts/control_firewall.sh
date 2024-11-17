#!/bin/bash

# Variables
SERVER_IP="192.168.1.20"  # IP address of Device 2
USERNAME="your_username"  # SSH username for Device 2

# Usage function
function usage() {
    echo "Usage: $0 <option>"
    echo "Options:"
    echo "  1 - Basic Inbound/Outbound Rules"
    echo "  2 - IP Address Filtering"
    echo "  3 - Port-Based Filtering"
    echo "  4 - Protocol-Based Filtering"
    echo "  5 - Connection State Rules"
    echo "  6 - Time-Based Rules"
    echo "  7 - Reset All Rules"
    exit 1
}

# Check if an option is provided
if [ $# -eq 0 ]; then
    usage
fi

# Function to execute the script on Device 2
function run_remote_script() {
    local script_name=$1
    echo "Executing $script_name on Device 2..."
    ssh "${USERNAME}@${SERVER_IP}" "bash -s" < "$script_name"
}

# Execute based on user input
case $1 in
    1)
        run_remote_script "firewall_inbound_outbound.sh"
        ;;
    2)
        run_remote_script "firewall_ip_filter.sh"
        ;;
    3)
        run_remote_script "firewall_port_filter.sh"
        ;;
    4)
        run_remote_script "firewall_protocol_filter.sh"
        ;;
    5)
        run_remote_script "firewall_conntrack.sh"
        ;;
    6)
        run_remote_script "firewall_time_filter.sh"
        ;;
    7)
        run_remote_script "firewall_reset.sh"
        ;;
    *)
        echo "Invalid option!"
        usage
        ;;
esac

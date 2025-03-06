1. Changing MAC Address on Linux
Method 1: Using ip Command (Temporary Change)
Open a terminal.

Identify your network interface:

bash
Copy
ip link show
Look for the interface name (e.g., eth0, wlan0).

Disable the interface:

bash
Copy
sudo ip link set dev <interface> down
Replace <interface> with your interface name.

Change the MAC address:

bash
Copy
sudo ip link set dev <interface> address <new_mac_address>
Replace <new_mac_address> with the desired MAC address (e.g., 00:11:22:33:44:55).

Re-enable the interface:

bash
Copy
sudo ip link set dev <interface> up
Verify the change:

bash
Copy
ip link show <interface>
Method 2: Using macchanger (Permanent or Random Change)
Install macchanger:

bash
Copy
sudo apt install macchanger
Change the MAC address:

bash
Copy
sudo macchanger -r <interface>
This sets a random MAC address. Use -m to specify a custom MAC address:

bash
Copy
sudo macchanger -m <new_mac_address> <interface>
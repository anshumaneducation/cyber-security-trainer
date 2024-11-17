Prerequisites

Before running these scripts, ensure:

    You have root privileges (sudo access) on your Kali Linux machine.
    iptables is installed (it should be by default on Kali).
    Back up current iptables rules before running the scripts:

`sudo iptables-save > ~/iptables_backup.rules`

After running the scripts, restore your original rules if needed:

`sudo iptables-restore < ~/iptables_backup.rules`

Customize the scripts to experiment with different IPs, ports, and protocols.
Use `iptables -L -v -n` to view active rules after running a script.
Use `sudo iptables-save > myrules.rules` to save your current rules configuration.
Always reset rules using `firewall_reset.sh` after experimenting.


Step 1: Prerequisites

Make sure:

    SSH is enabled on Device 2.
    Device 1 has SSH access to Device 2 (passwordless SSH setup is recommended using SSH keys).
    iptables is installed on Device 2.
    Device 2’s firewall should allow SSH access (port 22) from Device 1.
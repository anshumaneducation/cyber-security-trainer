how to run and verify bash scripts

Here’s a detailed `README.md` file you can use to guide cybersecurity professionals on how to run and verify the bash scripts for practical learning. The steps will ensure that they can execute and understand the functionality of each script.

```markdown
# Network and Port Scanning Bash Scripts

This repository contains a collection of bash scripts designed for practical exercises in network identification, host discovery, and port scanning. These scripts are tailored to help cybersecurity professionals learn about various techniques for network reconnaissance, port scanning, and service identification.

## Prerequisites

Before running the scripts, ensure that your system has the following tools installed:

- **Netcat (nc)**: Required for TCP ping and scanning.
  - Install on Ubuntu:
    ```bash
    sudo apt-get install netcat
    ```
- **Nmap**: Used for port scanning and OS detection.
  - Install on Ubuntu:
    ```bash
    sudo apt-get install nmap
    ```

## List of Scripts

### 1. `tcp_ping.sh` - TCP Ping
   This script uses Netcat to check if a host is reachable on ports 80 and 443.

   **Usage:**
   ```bash
   ./tcp_ping.sh <target>
   ```

   Example:
   ```bash
   ./tcp_ping.sh 192.168.1.1
   ```

### 2. `ping_sweep.sh` - Ping Sweep
   This script performs a ping sweep to find live hosts in a subnet.

   **Usage:**
   ```bash
   ./ping_sweep.sh <network>
   ```

   Example:
   ```bash
   ./ping_sweep.sh 192.168.1
   ```

### 3. `icmp_ping.sh` - ICMP Ping
   This script checks if a host is reachable using ICMP (ping).

   **Usage:**
   ```bash
   ./icmp_ping.sh <target>
   ```

   Example:
   ```bash
   ./icmp_ping.sh 192.168.1.1
   ```

### 4. `null_scan.sh` - Null Scan
   Performs a null scan to check open ports without sending any flags.

   **Usage:**
   ```bash
   ./null_scan.sh <target>
   ```

   Example:
   ```bash
   ./null_scan.sh 192.168.1.1
   ```

### 5. `fast_scan.sh` - Fast Scan
   This script performs a quick scan to identify open ports using the `-F` option in Nmap.

   **Usage:**
   ```bash
   ./fast_scan.sh <target>
   ```

   Example:
   ```bash
   ./fast_scan.sh 192.168.1.1
   ```

### 6. `udp_scan.sh` - UDP Port Scan
   Performs a scan to identify open UDP ports.

   **Usage:**
   ```bash
   ./udp_scan.sh <target>
   ```

   Example:
   ```bash
   ./udp_scan.sh 192.168.1.1
   ```

### 7. `syn_scan.sh` - SYN Stealth Scan
   This script performs a SYN stealth scan to detect open ports without completing the handshake.

   **Usage:**
   ```bash
   ./syn_scan.sh <target>
   ```

   Example:
   ```bash
   ./syn_scan.sh 192.168.1.1
   ```

### 8. `fin_scan.sh` - FIN Stealth Scan
   Performs a FIN stealth scan to detect open ports by sending FIN packets.

   **Usage:**
   ```bash
   ./fin_scan.sh <target>
   ```

   Example:
   ```bash
   ./fin_scan.sh 192.168.1.1
   ```

### 9. `os_detection.sh` - OS Detection
   This script attempts to identify the operating system of the target host.

   **Usage:**
   ```bash
   ./os_detection.sh <target>
   ```

   Example:
   ```bash
   ./os_detection.sh 192.168.1.1
   ```

---

## Running the Scripts

### Step 1: Download the Scripts
Clone or download this repository to your local machine.

### Step 2: Make the Scripts Executable
After downloading, ensure that the scripts are executable. Run the following command in the terminal:

```bash
chmod +x *.sh
```

### Step 3: Run the Scripts
You can run each script by executing the following command format:

```bash
./<script_name>.sh <target>
```

For example:
```bash
./tcp_ping.sh 192.168.1.1
```

### Step 4: Review Output
- Each script provides useful output for understanding the status of the target host or open ports.
- For example, a successful TCP ping will show:
  ```
  Performing TCP Ping on 192.168.1.1 for ports 80 and 443...
  Connection to 192.168.1.1 80 port [tcp/http] succeeded!
  Connection to 192.168.1.1 443 port [tcp/https] succeeded!
  ```

  If the port is closed or the host is unreachable, the script will print a message indicating that.

---

## Verifying the Results

### 1. **Check for Open Ports**
   After running the scan scripts (e.g., SYN, FIN, UDP scan), verify the results by running:

   ```bash
   nmap -p <port_range> <target>
   ```

   Example:
   ```bash
   nmap -p 80,443 192.168.1.1
   ```

   This will confirm whether the ports are open based on the results you got from the scripts.

### 2. **Cross-check with Online Tools**
   For some basic tests, you can cross-check results by using online port scanning tools like [Shodan](https://www.shodan.io) to verify if certain ports are open on a public host.

---

## Troubleshooting

- **Permissions Issue**: Some scans, like SYN Stealth, may require root privileges. Use `sudo` when running these scripts:
  ```bash
  sudo ./syn_scan.sh 192.168.1.1
  ```
  
- **Host Unreachable**: If a target is unreachable, check if the host is up using `ping`:
  ```bash
  ping 192.168.1.1
  ```

- **Firewall Issues**: Ensure that your firewall settings on both the scanning machine and the target machine are configured to allow the scan.

---

## Conclusion

These scripts are designed to simulate common penetration testing methods in cybersecurity. By running and modifying them, you'll get hands-on experience with network discovery, host identification, and port scanning techniques. Always be sure to use these scripts in a legal and ethical environment, such as your own network or with explicit permission from the network owner.





### Key Sections Explained:

- **Prerequisites**: Ensures that the necessary tools like `nc` (Netcat) and `nmap` are installed.
- **Scripts Overview**: Explains each script's functionality with sample commands.
- **Running the Scripts**: Provides step-by-step instructions to execute the scripts on a target host or network.
- **Verifying the Results**: Suggests how to verify the output with Nmap or online tools.
- **Troubleshooting**: Offers common solutions for problems such as permissions or firewall issues.

This `README.md` provides a clear structure to guide cybersecurity professionals through the practical exercises using the bash scripts.



Here's a breakdown of what each script and its output is doing:

1. **`./tcp_ping.sh 192.168.1.1`**:
   - This script attempts a TCP Ping on ports 80 (HTTP) and 443 (HTTPS) of the host `192.168.1.1`.
   - **Output**: Both ports are either closed or the host is unreachable.

2. **`./ping_sweep.sh 192.168.1`**:
   - This performs a "ping sweep" on the network `192.168.1.x` to check which devices are active. However, no detailed output is shown in your case, indicating either no response or that it's in the middle of the sweep without providing results yet.

3. **`./icmp_ping.sh 192.168.1.1`**:
   - This script sends an ICMP Ping (standard "ping" command) to `192.168.1.1` to check connectivity.
   - **Output**: 100% packet loss means the host is either down, unreachable, or blocking ICMP requests.

4. **`./null_scan.sh 192.168.1.1`**:
   - A Null Scan, which doesn't set any flags in the TCP header, is used to try to gather information about open ports.
   - **Output**: The script requires root privileges, so it quits without scanning.

5. **`sudo ./null_scan.sh 192.168.1.1`**:
   - Running the Null Scan with `sudo` allows the scan to proceed with root privileges.
   - **Output**: The scan finds all 1000 ports on `192.168.1.1` as either "open" or "filtered".

6. **`./fast_scan.sh 192.168.1.1`**:
   - This performs a fast scan on the host `192.168.1.1` to quickly check for open ports.
   - **Output**: The host seems down, possibly due to blocking of ping probes. The script suggests trying `-Pn` to bypass the ping check.

7. **`./udp_scan.sh 192.168.1.1`**:
   - A UDP port scan is performed to check open UDP ports.
   - **Output**: Requires root privileges, so the scan quits without running.

8. **`sudo ./udp_scan.sh 192.168.1.1`**:
   - Running the UDP Scan with `sudo` to get root privileges.
   - **Output**: All 1000 scanned UDP ports on `192.168.1.1` are either open or filtered.

9. **`./syn_scan.sh 192.168.1.1`**:
   - This script performs a SYN Stealth Scan, used to detect open ports without fully establishing connections.
   - **Output**: Requires root privileges, so it quits.

10. **`sudo ./syn_scan.sh 192.168.1.1`**:
    - Running the SYN Stealth Scan with `sudo` allows the scan to proceed.
    - **Output**: All 1000 ports are "filtered," meaning they are being blocked or are in a state that prevents detection.

11. **`./fin_scan.sh 192.168.1.1`**:
    - A FIN Stealth Scan is used, sending a FIN flag to detect open ports.
    - **Output**: Requires root privileges, so it quits.

12. **`sudo ./fin_scan.sh 192.168.1.1`**:
    - Running the FIN Stealth Scan with `sudo` allows the scan to proceed.
    - **Output**: All 1000 ports are either open or filtered.

13. **`./os_detection.sh`**:
    - This script attempts to detect the operating system of the host.
    - **Output**: Usage information is displayed because no target is provided.

14. **`sudo ./os_detection.sh 192.168.1.1`**:
    - Running the OS detection script with `sudo` allows it to gather more detailed information.
    - **Output**: The OS is detected as a Sony PlayStation 2 game console, indicating the target is likely a gaming device rather than a typical server or computer.

In summary, several scans require root privileges to run, which is why `sudo` is needed in most cases. Different types of scans (SYN, FIN, Null, UDP) return information about open or filtered ports, while others (like ICMP and TCP Ping) indicate whether the host is reachable or blocking certain traffic types. The OS detection identifies the target as a Sony PlayStation 2 game console based on its TCP/IP fingerprint.
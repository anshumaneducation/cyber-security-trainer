### Attack and Detection Setup Summary

#### Node 1: Attacker
1. **Attack Command**:
   Run the following on Node 1 (attacker):
   ```bash
   sudo hping3 -S -p 80 -f -a <attacker-ip> <victim-ip>
   ```
   - Replace `<attacker-ip>` with the attacker's IP address.
   - Replace `<victim-ip>` with the victim machine's IP address.

   **Explanation**:
   - `-S`: SYN flag set.
   - `-p 80`: Targets port 80.
   - `-f`: Fragment packets.
   - `-a`: Spoof the source address.

#### Node 2: IDS (Snort)
1. **Add a Rule**:
   Open the Snort rules file:
   ```bash
   sudo nano /etc/snort/rules/local.rules
   ```
   Add the following rule:
   ```bash
   alert tcp any any -> any 80 (msg:"Possible SYN Flood with Fragmentation"; flags:S; fragbits:M; ttl:<=64; sid:1000002; rev:1;)
   ```

2. **Include the Rules File in Configuration**:
   Open the Snort configuration file:
   ```bash
   sudo nano /etc/snort/snort.conf
   ```
   Ensure the rules file is included:
   ```bash
   include $RULE_PATH/local.rules
   ```
   If `$RULE_PATH` is not set, replace it with the actual path, such as:
   ```bash
   include /etc/snort/rules/local.rules
   ```

3. **Run Snort**:
   Start Snort on the appropriate interface:
   ```bash
   sudo snort -A console -q -c /etc/snort/snort.conf -i <interface>
   ```
   Replace `<interface>` with the network interface connected to the victim's network (e.g., `enp1s0` or `wlx503eaa61e484`).

#### Expected Outcome
- When the attacker sends SYN packets with fragmentation from Node 1, Snort on Node 2 should detect the activity and raise an alert.
- The alert will look like this in the Snort console output:
  ```
  [**] [1:1000002:1] Possible SYN Flood with Fragmentation [**]
  ```

### Troubleshooting Tips
1. **Verify Interface**:
   Ensure the interface specified in the Snort command is the one receiving traffic.

2. **Test Configuration**:
   Test the Snort configuration for syntax errors:
   ```bash
   sudo snort -T -c /etc/snort/snort.conf
   ```

3. **Monitor Traffic**:
   Use `tcpdump` on Node 2 to confirm fragmented packets are reaching the IDS:
   ```bash
   sudo tcpdump -i <interface> port 80
   ```

By following these steps, Node 2 will successfully detect and alert on the fragmented SYN flood attack initiated from Node 1.



### Adding an Additional Attack Type and Detection Rule

#### Attack 2: ICMP Flood
- **Description**: An ICMP flood attack overwhelms the victim with excessive ICMP Echo Request packets (commonly known as "ping flood").
  
---

### Node 1: Attacker
**Attack Command**:
```bash
sudo hping3 --icmp -flood -a <attacker-ip> <victim-ip>
```
- `--icmp`: Sends ICMP Echo Request packets.
- `-flood`: Sends packets as quickly as possible without waiting for replies.
- `-a`: Spoofs the source address.
- Replace `<attacker-ip>` and `<victim-ip>` accordingly.

---

### Node 2: IDS (Snort)

1. **Add Detection Rule**:
   Open the Snort rules file:
   ```bash
   sudo nano /etc/snort/rules/local.rules
   ```
   Add this rule to detect an ICMP flood:
   ```bash
   alert icmp any any -> any any (msg:"ICMP Flood Detected"; dsize:>1000; sid:1000003; rev:1;)
   ```
   **Explanation**:
   - `alert icmp`: Detect ICMP traffic.
   - `any any -> any any`: Matches all source and destination addresses and ports.
   - `dsize:>1000`: Triggers on ICMP packets larger than 1000 bytes (indicating potential flooding).
   - `msg`: Message to display in the alert.
   - `sid`: Unique rule identifier.
   - `rev`: Rule revision.

2. **Include the Rule in Configuration**:
   Ensure the rules file is included in `/etc/snort/snort.conf` as done previously:
   ```bash
   include /etc/snort/rules/local.rules
   ```

3. **Restart Snort**:
   Start Snort to monitor traffic:
   ```bash
   sudo snort -A console -q -c /etc/snort/snort.conf -i <interface>
   ```

---

### Expected Alerts for Both Attacks
#### Attack 1: SYN Flood with Fragmentation
```plaintext
[**] [1:1000002:1] Possible SYN Flood with Fragmentation [**]
```

#### Attack 2: ICMP Flood
```plaintext
[**] [1:1000003:1] ICMP Flood Detected [**]
```

---

### Verification and Testing
- Use `tcpdump` to confirm ICMP traffic reaches the IDS:
  ```bash
  sudo tcpdump -i <interface> icmp
  ```

- Test Snort rules for syntax errors:
  ```bash
  sudo snort -T -c /etc/snort/snort.conf
  ```

With these configurations, your Snort IDS will be able to detect both SYN Flood with fragmentation and ICMP flood attacks.
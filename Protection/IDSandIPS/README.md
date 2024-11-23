*sudo nano /etc/snort/rules/local.rules*

`# Detect Nmap SYN scans
alert tcp any any -> $HOME_NET any (msg:"Nmap SYN Scan Detected"; flags:S; sid:1000001; rev:1;)

# Detect Netcat connection attempts
alert tcp any any -> $HOME_NET 1234 (msg:"Netcat Backdoor Attempt"; sid:1000002; rev:1;)

# Detect malicious TCP flood
alert tcp any any -> $HOME_NET any (msg:"TCP Flood Detected"; threshold:type threshold, track by_src, count 50, seconds 2; sid:1000003; rev:1;)`

Learning Outcomes

    Attacker's Perspective:
        Understand various attack vectors (e.g., scans, floods, backdoors).
    Defender's Perspective:
        Analyze Snort alerts and logs.
        Learn to write custom rules for specific threats.
    Target's Perspective:
        Observe attack impacts and log malicious traffic.

# Running the Lab
Step 1: Set Up Network

    Ensure all machines are in the same network.
    Assign static IPs (e.g., 192.168.1.3 for Attacker, 192.168.1.2 for Defender, 192.168.1.4 for Target).

Step 2: Start Defender

Run the Defender script to activate Snort:

bash defender_setup.sh

Step 3: Start Target

Run the Target script to simulate vulnerable services:

bash target_setup.sh

Step 4: Simulate Attacks

Run the Attacker script to generate malicious traffic:

bash attacker_simulation.sh

Step 5: Observe Logs

    On the Defender machine, view Snort alerts in real time.
    On the Target machine, use tcpdump to analyze incoming traffic.

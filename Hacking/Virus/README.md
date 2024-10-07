# **Malware Simulation using Tkinter and Sockets**

This project demonstrates how **viruses**, **worms**, and **trojans** operate through a simulation, focusing on malware creation, propagation, and execution. The goal is to help students understand the technical mechanisms behind these types of malware in a hands-on manner, rather than just relying on theoretical knowledge.

## **Project Overview**

The simulation consists of three nodes:
1. **Attacker Node**: This node creates malware payloads (e.g., viruses, worms, trojans) and sends them to the target nodes.
2. **User Node**: Receives and executes malware, simulating system infection and file corruption.
3. **Server Node**: Simulates how worms spread across a network by creating new directories on the server, mimicking worm propagation.

### **Malware Types Simulated:**
- **Virus**: Infects a system by creating several dummy files that simulate corrupted or damaged files.
- **Worm**: Replicates itself across the network by creating directories on target machines, simulating the spread of the worm.
- **Trojan**: Acts as a malicious payload, performing harmful actions like adding backdoors, logging keystrokes, etc. (In this simulation, it creates a log entry for simplicity).

---

## **Project Files**

- **`attacker.py`**: GUI-based attacker node that creates and sends malware payloads.
- **`user.py`**: GUI-based user node that receives and executes the payload, simulating infection.
- **`server.py`**: GUI-based server node that simulates how worms replicate across the network.
  
### **Dependencies:**
- **Python 3.7+**
- **Tkinter**: For GUI elements.
- **Socket Library**: For communication between nodes.
  
You can install the required dependencies using:

How It Works

    Attacker Node:
        Creates a malware payload based on the chosen attack type (virus, worm, or trojan).
        Uses socket programming to send the payload to the user or server nodes.

    User Node:
        Listens for incoming payloads.
        Once a payload is received, it is executed, simulating how malware infects a system (e.g., by creating corrupted files).

    Server Node:
        Similar to the user node but focuses on simulating worm replication.
        Once a worm payload is received, the worm spreads by creating directories, simulating network-wide infection.

Example Simulation:

    The Attacker sends a Virus payload to the User Node.
    The User Node receives and executes the payload, creating multiple dummy files (infected_file_1.txt, etc.), simulating how a virus spreads across a system.
    Similarly, the attacker can send a Worm to the Server Node, which will then create new directories, simulating the worm's replication across the network.

Security Disclaimer

This project is intended for educational purposes only. It simulates how viruses, worms, and trojans work to help students understand the risks of malware and how they are implemented. Do not use any part of this project for malicious purposes or in any real-world network or system environment.
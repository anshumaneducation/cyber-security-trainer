import os
import hashlib
import json

# Load the malware hashes from the JSON file
with open('malware_hashes.json', 'r') as file:
    malware_hashes = json.load(file)

def scan_files():
    # Traverse through all files in the current working directory and its subdirectories
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            # Compute the MD5 hash of the file
            file_hash = hashlib.md5(open(os.path.join(root, file), 'rb').read()).hexdigest()
            
            # Check if the file hash matches any malware hash
            if file_hash in malware_hashes.values():
                print(f"Malware detected: {file}")
                # Add your desired action here, e.g., deleting the file
                os.remove(os.path.join(root, file))

scan_files()

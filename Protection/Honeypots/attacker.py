# attacker.py
import requests

TARGET_URL = "http://127.0.0.1:8080/vulnerable"

def attack():
    print("Simulating attack...")
    payload = {"username": "admin1", "password": "password1234"}
    try:
        response = requests.post(TARGET_URL, json=payload)
        print(f"Response from victim: {response.status_code} - {response.text}")
    except requests.ConnectionError:
        print("Failed to connect to the target.")

if __name__ == '__main__':
    attack()

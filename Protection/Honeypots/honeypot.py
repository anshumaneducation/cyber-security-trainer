# honeypot.py
from flask import Flask, request
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(filename="honeypot_logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

@app.route('/', methods=['GET', 'POST'])
def honeypot():
    # Log incoming requests
    logging.info(f"Received {request.method} request from {request.remote_addr}")
    if request.data:
        logging.info(f"Data: {request.data.decode('utf-8')}")
    return "Access Denied", 403

@app.route('/vulnerable', methods=['POST'])
def vulnerable():
    # Simulate a vulnerable endpoint
    logging.info(f"Attack attempt: {request.data.decode('utf-8')}")
    return "Data received", 200

if __name__ == '__main__':
    # Run on port 8080
    app.run(host='0.0.0.0', port=8080)

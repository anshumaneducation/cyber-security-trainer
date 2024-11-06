# mqtt_client.py
import paho.mqtt.client as mqtt

# Define the MQTT settings
broker = "localhost"  # Change to the broker's IP if not running locally
port = 1883           # Default MQTT port

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to a topic after connecting
    client.subscribe("test/topic")

# Callback function when a message is received
def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker, port, 60)

# Start the loop to process callbacks
client.loop_start()

# Publish a test message
client.publish("test/topic", "Hello MQTT!")

# Keep the script running to listen for messages
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()

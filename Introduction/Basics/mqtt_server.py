import asyncio
from hbmqtt.broker import Broker

# Broker configuration
config = {
    "listeners": {
        "default": {
            "type": "tcp",
            "bind": "0.0.0.0:1883"  # Standard MQTT port
        }
    },
    "sys_interval": 10,
    "auth": {
        "allow-anonymous": True  # Allows anonymous connections
    }
}

broker = Broker(config)

# Start the broker
async def start_broker():
    await broker.start()
    print("MQTT Broker running on port 1883...")

loop = asyncio.get_event_loop()
loop.run_until_complete(start_broker())
loop.run_forever()

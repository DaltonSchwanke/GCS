import socket
import json
import random
import time
from datetime import datetime
from dotenv import load_dotenv
import os

# === Load environment variables from .env ===
load_dotenv()

PI_IP = os.getenv("PI_IP")
PI_PORT = int(os.getenv("PI_PORT"))

if not PI_IP or not PI_PORT:
    raise ValueError("Missing PI_IP or PI_PORT in .env file")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def generate_fake_telemetry():
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "altitude": round(random.uniform(1000, 10000), 2),    # feet
        "speed": round(random.uniform(100, 350), 2),          # knots
        "latitude": round(random.uniform(44.9, 45.0), 6),     # near MN
        "longitude": round(random.uniform(-93.3, -93.1), 6),  # near MN
        "heading": round(random.uniform(0, 359), 2)           # degrees
    }

print(f"Sending telemetry to {PI_IP}:{PI_PORT} ... (Press Ctrl+C to stop)")

try:
    while True:
        telemetry = generate_fake_telemetry()
        message = json.dumps(telemetry).encode('utf-8')
        sock.sendto(message, (PI_IP, PI_PORT))
        print(f"[SENT] {telemetry}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTransmission stopped by user.")
finally:
    sock.close()
import socket
import json
from dotenv import load_dotenv
import os

# === Load environment variables from .env ===
load_dotenv()

PI_IP = os.getenv("PI_IP")        # This should match the IP used in simulate_aircraft
PI_PORT = int(os.getenv("PI_PORT"))

if not PI_IP or not PI_PORT:
    raise ValueError("Missing PI_IP or PI_PORT in .env file")

# === Set up the UDP server socket ===
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((PI_IP, PI_PORT))

print(f"Listening for telemetry on {PI_IP}:{PI_PORT}...")

try:
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size = 1024 bytes
        try:
            telemetry = json.loads(data.decode('utf-8'))
            print(f"[RECEIVED from {addr}] → {json.dumps(telemetry, indent=2)}")
        except json.JSONDecodeError:
            print(f"[WARNING] Received non-JSON data: {data}")
except KeyboardInterrupt:
    print("\nTelemetry receiver stopped.")
finally:
    sock.close()
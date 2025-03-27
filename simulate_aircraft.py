import random
import time
import json

# Function to simulate aircraft telemetry
def generate_telemetry():
    # Mock data to simulate telemetry (altitude, speed, position)
    telemetry = {
        "altitude": random.randint(1000, 35000),
        "speed": random.randint(200, 600),
        "latitude": random.uniform(30.0, 60.0),
        "longitude": random.uniform(-120.0, -60.0),
        "timestamp": time.time()
    }
    return telemetry

# Function to send telemetry data (could be to a server or GCS)
def send_telemetry(data):
    # For now, we'll just print the data to simulate sending
    print(f"Sending telemetry data: {data}")

def main():
    while True:
        # Generate random telemetry
        telemetry_data = generate_telemetry()
        send_telemetry(telemetry_data)
        time.sleep(1)  # Simulate a delay of 1 second between telemetry updates

if __name__ == "__main__":
    main()
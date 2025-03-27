import time
import json

# Example function to simulate receiving telemetry data
def receive_telemetry():
    
    # Mock Data for Testing GCS File
    data = {
        "altitude": 10000, 
        "speed": 250,
        "latitude": 45.0,
        "longitude": -93.0,
        "timestamp": time.time()
    }
    return data



# Function to log telemetry data
def log_telemetry(data):
    with open("telemetry_log.json", "a") as log_file:
        log_file.write(json.dumps(data) + "\n")



# Function to process and display telemetry data
def display_telemetry(data):
    print(f"Altitude: {data['altitude']} ft")
    print(f"Speed: {data['speed']} km/h")
    print(f"Latitude: {data['latitude']}°")
    print(f"Longitude: {data['longitude']}°")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['timestamp']))}")
    print("-" * 40)


def main():
    while True:
        telemetry_data = receive_telemetry()
        log_telemetry(telemetry_data)
        display_telemetry(telemetry_data)
        time.sleep(1) 


if __name__ == "__main__":
    main()
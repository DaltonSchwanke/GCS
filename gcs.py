import socket
import json
from dotenv import load_dotenv
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QTimer

# === Load environment variables from .env ===
load_dotenv()

PI_IP = "10.0.0.215"  # os.getenv("PI_IP")
PI_PORT = 5005        # int(os.getenv("PI_PORT"))

if not PI_IP or not PI_PORT:
    raise ValueError("Missing PI_IP or PI_PORT in .env file")

# === GUI Map Window ===
class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GCS Telemetry Map")
        self.resize(800, 600)

        self.view = QWebEngineView()
        local_url = QUrl.fromLocalFile(os.path.abspath("map.html"))
        self.view.load(local_url)

        self.setCentralWidget(self.view)

    def update_map(self, lat, lon, speed, angle):
        js = f"updateMarker({lat}, {lon}, {speed}, {angle});"
        self.view.page().runJavaScript(js)

# === Set up the UDP server socket ===
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((PI_IP, PI_PORT))

print(f"Listening for telemetry on {PI_IP}:{PI_PORT}...")

# === PyQt Application ===
app = QApplication(sys.argv)
window = MapWindow()
window.show()

# === Periodic Socket Polling ===
def poll_socket():
    try:
        data, addr = sock.recvfrom(1024)  # Buffer size = 1024 bytes
        try:
            telemetry = json.loads(data.decode('utf-8'))
            print(f"[RECEIVED from {addr}] → {json.dumps(telemetry, indent=2)}")

            lat = telemetry.get("latitude", 0)
            lon = telemetry.get("longitude", 0)
            speed = telemetry.get("speed", 0)
            angle = telemetry.get("angle", 0)

            window.update_map(lat, lon, speed, angle)

        except json.JSONDecodeError:
            print(f"[WARNING] Received non-JSON data: {data}")
    except Exception as e:
        print(f"Error: {e}")

# === Start polling ===
timer = QTimer()
timer.timeout.connect(poll_socket)
timer.start(100)  # check every 100ms

try:
    sys.exit(app.exec_())
except KeyboardInterrupt:
    print("\nTelemetry receiver stopped.")
finally:
    sock.close()

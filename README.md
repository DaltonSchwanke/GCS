# GCS Telemetry Project

## Overview

This project simulates an aircraft's telemetry data and sends it to a Raspberry Pi-based Ground Control Station (GCS). 
The GCS receives, logs, and visualizes the telemetry data, while also enabling two-way communication for controlling the aircraft's behavior.

## Features
- Aircraft simulation generating random telemetry data.
- Raspberry Pi-based telemetry receiver and logger.
- Telemetry visualizer displaying live data.
- Two-way communication for aircraft control.

## Technologies
- Python for aircraft simulation and server-side logic.
- Flask (or Express) for server-side communication.
- Raspberry Pi for the GCS.
- (Optional) Visualization using JavaScript libraries (e.g., D3.js, Leaflet).

## Setup

1. Clone the repository.
2. Install dependencies.
3. Run the simulation and telemetry receiver.

## Usage

To run the simulation:
```bash
python simulate_aircraft.py

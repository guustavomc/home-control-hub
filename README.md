# Raspberry Pi Phone Presence Detector

This project uses a Raspberry Pi to detect the presence of a specific phone. Pi constantly scans for nearby Bluetooth devices. When the phone connects (arrives) or disconnects (leaves), it logs the event and can trigger custom automations, such as sending alerts or controlling smart home devices.

## Prerequisites

- Raspberry Pi with Raspbian OS installed
- Raspberry Pi with built-in Bluetooth
- Python 3 installed
- Your phone’s Bluetooth name
- python3-bluetooth package

## Setup Instructions

### Step 1: Install Required Tools

Install `arp-scan` to scan the network:

```bash
sudo apt update
sudo apt install python3-bluetooth
```

### Step 2: Identify Your Phone's Bluetooth name

Find your phone's name by scanning:

```bash
bluetoothctl
scan on
```

Watch the output and get your phone's name or MAC. Example:

```bash
[NEW] Device DC:A6:32:XX:XX:XX  John's iPhone
```

Locate your phone in the scan results and note its name and MAC address (e.g., `AA:BB:CC:DD:EE:FF`).

### Step 3: Configure the Script

1. Clone or download this repository to your Raspberry Pi.
2. Open the `presence_monitor.py` script and update the `TARGET_NAME` variable with your phone's name:

   ```python
   TARGET_NAME = "Phone Name"  # Replace with your phone's name
   ```

3. Optionally, adjust the `SCAN_INTERVAL` (default: 10 seconds) or `LOG_FILE` path.

### Step 4: Run the Script

Run the script with Python 3:

```bash
python3 presence_monitor.py
```

The script will:
- Scan the bluetooth every 10 seconds.
- Print if the device is nearby or not.

Press `Ctrl+C` to stop the script.

### Step 5: Add Automations

You can trigger actions when the phone arrives or leaves. Modify the `log_event` function in `presence_monitor.py` to include your automation. Examples:

- **Run a script** (e.g., turn on a light):

   ```python
   os.system("python3 turn_on_light.py")
   ```

- **Send a webhook** (e.g., to Home Assistant):

   ```python
   import requests
   requests.post("http://homeassistant.local:8123/api/webhook/your_custom_hook")
   ```

- Other ideas:
  - Send a Telegram or email alert.
  - Control a GPIO pin (e.g., LED or relay).
  - Integrate with smart home platforms via HTTP or MQTT.


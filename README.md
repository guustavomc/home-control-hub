# Raspberry Pi Phone Presence Detector

This project uses a Raspberry Pi to detect the presence of a specific phone on your local network by scanning for its MAC address. When the phone connects (arrives) or disconnects (leaves), it logs the event and can trigger custom automations, such as sending alerts or controlling smart home devices.

## Prerequisites

- Raspberry Pi with Raspbian OS installed
- Wi-Fi enabled on the Raspberry Pi
- Python 3 installed
- `arp-scan` package installed
- Sudo privileges for running network scans

## Setup Instructions

### Step 1: Install Required Tools

Install `arp-scan` to scan the network:

```bash
sudo apt update
sudo apt install arp-scan
```

### Step 2: Identify Your Phone's MAC Address

Find your phone's MAC address on the network by scanning:

```bash
sudo arp-scan --interface=wlan0 --localnet
```

Alternatively, use `nmap`:

```bash
sudo nmap -sn 192.168.1.0/24
```

Locate your phone in the scan results and note its MAC address (e.g., `AA:BB:CC:DD:EE:FF`).

### Step 3: Configure the Script

1. Clone or download this repository to your Raspberry Pi.
2. Open the `presence_monitor.py` script and update the `PHONE_MAC` variable with your phone's MAC address:

   ```python
   PHONE_MAC = "AA:BB:CC:DD:EE:FF"  # Replace with your phone's MAC address
   ```

3. Optionally, adjust the `SCAN_INTERVAL` (default: 10 seconds) or `LOG_FILE` path.

### Step 4: Run the Script

Run the script with Python 3:

```bash
python3 presence_monitor.py
```

The script will:
- Scan the network every 10 seconds.
- Log arrivals and departures to `presence_log.txt` in the format:

   ```
   2025-04-22 13:42:01 - Device connected (arrived)
   2025-04-22 14:55:47 - Device disconnected (left)
   ```

- Only log once per arrival or departure to avoid repetitive entries.

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

## Notes

- Ensure your Raspberry Pi has a stable Wi-Fi connection.
- The script requires `sudo` for `arp-scan`, so run it with appropriate permissions.
- If your phone uses a randomized MAC address, assign a static IP or disable randomization in your phone's Wi-Fi settings.
- For continuous operation, consider running the script as a service using `systemd` or a process manager like `pm2`.

## Example Log Output

The `presence_log.txt` file will contain entries like:

```
2025-04-22 13:42:01 - Device connected (arrived)
2025-04-22 14:55:47 - Device disconnected (left)
```

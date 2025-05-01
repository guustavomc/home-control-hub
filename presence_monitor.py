import os
import time
from datetime import datetime

PHONE_MAC = "AA:BB:CC:DD:EE:FF"  # Replace with your device MAC address
SCAN_INTERVAL = 10  # seconds between scans
LOG_FILE = "presence_log.txt"

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {event}\n")
    print(f"{timestamp} - {event}")

def is_device_connected(mac_address):
    result = os.popen("sudo arp-scan --interface=wlan0 --localnet").read()
    return mac_address.lower() in result.lower()

def main():
    previously_connected = False

    while True:
        try:
            connected = is_device_connected(PHONE_MAC)

            if connected and not previously_connected:
                log_event("Device connected (arrived)")
                previously_connected = True

            elif not connected and previously_connected:
                log_event("Device disconnected (left)")
                previously_connected = False

            time.sleep(SCAN_INTERVAL)
        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()

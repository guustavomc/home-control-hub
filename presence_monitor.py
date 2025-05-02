import os
import time

PHONE_IP = "192.168.1.254"

def is_phone_online():
    response = os.system(f"ping -c 1 -W 1 {PHONE_IP} > /dev/null 2>&1")
    return response == 0

while True:
    if is_phone_online():
        print("📶 Phone is online")
    else:
        print("🔌 Phone is offline")
    time.sleep(5)

import bluetooth
import time
import RPi.GPIO as GPIO

TARGET_NAME = "motorola edge 20 pro"
GPIO_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

def is_device_nearby():
    nearby_devices = bluetooth.discover_devices(duration=5, lookup_names=True)
    for addr, name in nearby_devices:
        if TARGET_NAME in name:
            return True
    return False

while True:
    if is_device_nearby():
        print("📱 Device found! Turning ON GPIO.")
        GPIO.output(GPIO_PIN, GPIO.HIGH)
    else:
        print("📴 Device not found. Turning OFF GPIO.")
        GPIO.output(GPIO_PIN, GPIO.LOW)
    time.sleep(10)

import smbus
import time

# Raspberry Pi's I2C address
DEVICE_ADDRESS = 0x08

# Create an I2C bus instance
bus = smbus.SMBus(1)  # Raspberry Pi 3 uses I2C bus 1

while True:
    data = bus.read_byte(DEVICE_ADDRESS)
    print("Vibration Sensor Value:", data)
    time.sleep(1)  # Adjust delay as needed

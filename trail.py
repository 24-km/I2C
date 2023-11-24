import smbus
import time

address = 0x9  # Replace this with the address used by your Arduino master
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

def receive_from_arduino():
    try:
        data = bus.read_byte(address)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None

try:
    while True:
        value = receive_from_arduino()
        if value is not None:
            print(f"Received Data from Arduino: {value}")
        time.sleep(1)  # Adjust the sleep time based on your requirements

except KeyboardInterrupt:
    print("Program terminated by the user.")

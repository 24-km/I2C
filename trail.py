import smbus
import time

address = 0x08  # Arduino I2C address
bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

def read_vibration_value():
    try:
        value = bus.read_byte(address)
        return value
    except Exception as e:
        print(f"Error: {e}")
        return None

try:
    while True:
        vibration_value = read_vibration_value()

        if vibration_value is not None:
            print(f"Vibration Value: {vibration_value}")

        time.sleep(1)  # Adjust the sleep time based on your needs

except KeyboardInterrupt:
    print("Program terminated by the user.")
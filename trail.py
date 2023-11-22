from smbus import SMBus
import time

addr = 0x8  # Arduino's I2C address
bus = SMBus(1)  # I2C bus number (Raspberry Pi 4 uses bus 1)

def receive_sensor_data():
    try:
        while True:
            data = bus.read_byte(addr)  # Read sensor data from Arduino
            print("Received Vibration Sensor Value:", data)
            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    receive_sensor_data()

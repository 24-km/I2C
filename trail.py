from smbus import SMBus
import time

bus = SMBus(1)
address = 0x08  # Arduino's I2C address

def receive_sensor_data():
    try:
        while True:
            # Read two bytes from Arduino (higher and lower bytes)
            high_byte = bus.read_byte(address)
            low_byte = bus.read_byte(address)
            
            # Combine two bytes to get the sensor value
            sensor_value = (high_byte << 8) | low_byte
            
            # Print received sensor data
            print("Received Vibration Sensor Value:", sensor_value)
            
            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    receive_sensor_data()

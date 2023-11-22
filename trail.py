from smbus import SMBus
import time

addr = 0x8  # Arduino's I2C address
bus = SMBus(1)  # I2C bus number (Raspberry Pi 4 uses bus 1)

while True:
    bus.write_byte(addr, ord('R'))  # Sending 'R' to request sensor data from Arduino
    time.sleep(1)  # Give time for Arduino to process and respond
    
    # Read a byte from the Arduino (response from the vibration sensor)
    sensor_data = bus.read_byte(addr)
    
    # Print the received sensor data
    print("Vibration Sensor Value:", sensor_data)
    time.sleep(1)  # Adjust delay as needed

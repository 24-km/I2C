import smbus
import time
import sys

bus = smbus.SMBus(1)
address = 0x04  # Arduino I2C Address

def main():
    while True:
        # Request data from Arduino
        data = bus.read_byte(address)
        print("Received from Arduino:", data)
        
        time.sleep(1)  # Adjust delay as needed

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

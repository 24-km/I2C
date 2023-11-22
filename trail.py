import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)  # Serial port and baud rate

def receive_sensor_data():
    try:
        while True:
            if ser.in_waiting > 0:
                # Read and print sensor data received from Arduino
                sensor_data = ser.readline().decode('utf-8').rstrip()
                print("Received Vibration Sensor Value:", sensor_data)
            
            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    receive_sensor_data()

import serial
import time

# Serial port and baud rate
ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with the appropriate port

def receive_data():
    try:
        while True:
            if ser.in_waiting > 0:
                # Read received data from Arduino via serial
                received_data = ser.readline().decode('utf-8').rstrip()
                process_received_data(received_data)
            
            time.sleep(0.1)  # Adjust delay as needed
    except KeyboardInterrupt:
        pass

def process_received_data(data):
    # Interpret the received data based on the type of sensor
    sensor_data = data.split(':')
    if len(sensor_data) == 2:
        sensor_type, value = sensor_data[0], sensor_data[1]
        
        if sensor_type == 'SPEED':
            print(f"SPEED: {value}")
        elif sensor_type == 'Vibration Sensor':
            print(f"Vibration Sensor: {value}")
        elif sensor_type == 'Sound Sensor':
            print(f"Sound Sensor: {value}")

if __name__ == "__main__":
    receive_data()

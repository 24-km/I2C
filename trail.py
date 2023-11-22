import serial
import time

# Establish serial connection with the Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace '/dev/ttyACM0' with the correct port

def receive_sensor_data():
    try:
        while True:
            if ser.in_waiting > 0:
                # Read data from Arduino
                data = ser.readline().decode('utf-8').rstrip()
                process_sensor_data(data)
            
            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        ser.close()

def process_sensor_data(data):
    # Split the received data based on the sensor identifier
    sensor_data = data.split(':')
    if len(sensor_data) == 2:
        sensor_type, value = sensor_data[0], sensor_data[1]
        
        if sensor_type == 'VIBRATION':
            print(f"Received Vibration Sensor Value: {value}")
            # Add your processing or logic for vibration sensor data here
        elif sensor_type == 'SPEED':
            print(f"Received Speed Value: {value}")
            # Add your processing or logic for speed data here
        elif sensor_type == 'SOUND':
            print(f"Received Sound Sensor Value: {value}")
            # Add your processing or logic for sound sensor data here

if __name__ == "__main__":
    receive_sensor_data()

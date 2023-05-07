import serial

serial_port = 'COM6'  # replace with your Arduino serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def send_command(command):
    ser.write(command.encode())
def receive_data():
    data = ser.readline().decode('latin-1').strip()
    print(data)
    return data


# send a command to the Arduino board to read the sensor data
send_command('read_sensor_data')

# receive the sensor data from the Arduino board
sensor_data = receive_data()

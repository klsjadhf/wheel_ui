import serial
import time
import re

com_port = "/dev/tty.usbserial-A10JY27E"
baud_rate = 57600

counter = 0
test_str = "FC_V : 24.40 V |   FCT1:  27.83 C   |   H2P1  :  0.58 B |   DCDCV: XX.X V   |  FC_A  :  1.04 A |   FCT2:  28.22 C   |   H2P2  :  0.58 B |   DCDCA: XX.X A   |  FC_W  :  25.5 W |   FAN :    14 %    |   Tank-P:  12.9 B |   DCDCW: XXXX.X W |  Energy:     0 Wh|   BLW :    28 %    |   Tank-T:  0.00 C |   BattV:  23.49 V | "

def extract_val(name, string):
    start_index = test_str.find(name)
    end_index = test_str.find("|", start_index)
    extract_str = test_str[start_index : end_index]
    float_val = re.findall("\d+\.\d+", test_str[start_index : end_index])[0]
    print(start_index, end_index, extract_str, float_val)
    return float_val


def write_command(string_to_write):
    for char in string_to_write:
        ser.write(str.encode(char))
    ser.write(b'\r')

def read_to_newline():

    read_buffer = []
    last_read_char = b'x'

    while(last_read_char != '\r'):
        last_read_char = str(ser.read().decode())

        if (last_read_char == ''):
            break
        else:
            read_buffer.append(last_read_char)

    return ''.join(str(char) for char in read_buffer)

def recv_fuel_cell():
    while(True):
        time.sleep(0.5)
        if not ('ser' in globals()):
            continue
        
        read_str = read_to_newline()
        if len(read_str) > 0:
            print(read_str)

print("start fcc")
try:
    ser = serial.Serial(com_port, baudrate=baud_rate, timeout=0.1, writeTimeout=0.1)
    write_command('ver')
    
except serial.serialutil.SerialException as e:
    print('Cannot open port')
    print (e)

print ("FCT:", extract_val("FCT1", test_str))
print ("FC_W:", extract_val("FC_W", test_str))





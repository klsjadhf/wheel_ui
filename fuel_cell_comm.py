import serial
import time
import re

com_port = "/dev/tty0"
baud_rate = 115200

counter = 0
test_str = "FC_V : 24.40 V |   FCT1:  27.83 C   |   H2P1  :  0.58 B |   DCDCV: XX.X V   |  FC_A  :  1.04 A |   FCT2:  28.22 C   |   H2P2  :  0.58 B |   DCDCA: XX.X A   |  FC_W  :  25.5 W |   FAN :    14 %    |   Tank-P:  12.9 B |   DCDCW: XXXX.X W |  Energy:     0 Wh|   BLW :    28 %    |   Tank-T:  0.00 C |   BattV:  23.49 V | "

def extract_val(name, string):
    start_index = test_str.find(name)
    end_index = test_str.find("|", start_index)
    extract_str = test_str[start_index : end_index]
    float_val = re.findall("\d+\.\d+", test_str[start_index : end_index])[0]
    print(start_index, end_index, extract_str, float_val)
    return float_val


def recv_fuel_cell():
    global counter
    counter = counter + 1
    return counter

print("start fcc")
try:
    ser = serial.Serial(com_port, baudrate=baud_rate, timeout=1, writeTimeout=1)  # open serial port
    print("using :" + ser.name)         # check which port was really used
    ser.write(b'F')
except serial.serialutil.SerialException as e:
    print('Cannot open port')
    print (e)

print ("FCT:", extract_val("FCT1", test_str))
print ("FC_W:", extract_val("FC_W", test_str))




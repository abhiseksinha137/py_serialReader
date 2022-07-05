import serial
import time
ser = serial.Serial("COM3", 115200)
while True:
     cc=str(ser.readline())
     val=cc[2:][:-5]
     parts=val.replace('\\t', ',')
     part1=parts[0]
     part2=parts[1]

     # print(part1, part2)
     print(parts)
     time.sleep(1)
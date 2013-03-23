#!/usr/bin/python

import serial

ser = serial.Serial('/dev/ttyUSB0', timeout=5) # connect to receiver with 9600,N,8,1
ser.write("@PWR:1\r\n") # set to standby
ser.close() # close the connection

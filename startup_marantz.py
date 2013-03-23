#!/usr/bin/python

import serial

import time

ser = serial.Serial('/dev/ttyUSB0', timeout=5) # connect to receiver with 9600,N,8,1
ser.write("@PWR:2\r\n") # turn on from standby. there is a setting on the receiver to accept commands in standby mode
ser.close() # close the connection

time.sleep(10) # the receiver seems to need some time to process the commands

ser = serial.Serial('/dev/ttyUSB0', timeout=5)
ser.write("@VOL:0-35\r\n") # set the volume to -35dB
ser.close()

time.sleep(10)

ser = serial.Serial('/dev/ttyUSB0', timeout=5)
ser.write("@SRC:DD\r\n") # set the source to CD-R
ser.close()





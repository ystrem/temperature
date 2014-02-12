#!/usr/bin/env bash
import os
import glob
import time


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

thermometers = ['28-0000035ac85e', '28-0000035ac8a7', '28-0000035acb40']
temperatures = []
base_dir = '/sys/bus/w1/devices/'
device_file = '/w1_slave'

def temperature():
	for thermometer in thermometers:
		with open(base_dir + thermometer + device_file) as f:
			lines = f.readlines()
			temp =  [line.split() for line in lines ]
			#print 'Temp:', temp
			if 'YES' in temp[0]:
				temperature = float(temp[1][-1][2:]) / 1000
				temperatures.append(temperature)
			f.close()
			print 'File is closed = ', f.closed
	print temperatures
			#print 'Lines', lines			
	
	with open('temp.log', 'a') as f:
		print time.strftime('%Y-%m-%d %H:%M:%S ,', time.localtime()) + str('%s , %s , %s' %(temperatures[0], temperatures[1], temperatures[2]) )
		f.writelines(str(time.strftime('%Y-%m-%d %H:%M:%S ,', time.localtime()) + str('%s, %s, %s' %(temperatures[0], temperatures[1], temperatures[2]))) + '\n' )
		f.close()
		print 'File is closed = ', f.closed

	
if __name__ == '__main__':
	temperature()

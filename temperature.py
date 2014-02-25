#!/usr/bin/env bash
import os
import glob
import time
import sqllite3 as lite

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

thermometers = ['28-0000035ac85e', '28-0000035ac8a7', '28-0000035acb40']
temperatures = []
base_dir = '/sys/bus/w1/devices/'
device_file = '/w1_slave'

def saveToDB(data):
	con = lite.connect('temp.db')
	
	with con :
		cur = con.cursor()
		
		cur.execute("CREATE TABLE IF NOT EXISTS Temperatures(Date TEXT, Inside TEXT, Outside TEXT)")
		cur.execute("INSERT INTO Temperatures(Date, Inside, Outside) VALUES(?, ?, ?)", data)
		
		con.commit()

def temperature():
	temperatures.append(str(time.strftime('%Y-%m-%d %H:%M:%S ,', time.localtime())))
	for thermometer in thermometers:
		with open(base_dir + thermometer + device_file,'r') as f:
			lines = f.readlines()
			temp =  [line.split() for line in lines ]
			#print 'Temp:', temp
			if 'YES' in temp[0]:
				temperature = float(temp[1][-1][2:]) / 1000
				temperatures.append(temperature)
			f.close()
			print 'File is closed = ', f.closed
		
	return temperatures
		
if __name__ == '__main__':
	saveToDB(temperature())
	

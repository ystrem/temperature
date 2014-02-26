#!/usr/bin/env bash
import os
import glob
import time
import sqlite3 as lite

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

thermometers = ['28-0000035ac85e','28-0000035acb40']
temperatures = []
base_dir = '/sys/bus/w1/devices/'
device_file = '/w1_slave'
DB_NAME = 't.db'

def saveToDB(data):
	con = lite.connect(DB_NAME)
	
	with con:
		cur = con.cursor()
		
		cur.execute("CREATE TABLE IF NOT EXISTS Temperatures(Date DATE, Inside TEXT, Outside TEXT)")
		cur.execute("INSERT INTO Temperatures(Date, Inside, Outside) VALUES(datetime('now','localtime'), ?, ?)", data)
		
		con.commit()

def readFromDB():
	temp = []
	con = lite.connect(DB_NAME)
	
	with con:
		cur = con.cursor()
		
		week = cur.execute("SELECT * FROM Temperatures ORDER BY DATE LIMIT 25200")
		day = cur.execute("SELECT * FROM Temperatures ORDER BY DATE LIMIT 3600")
		
	print day
	
	with open('t.log','w') as f:

		for item in day:
			f.writelines(item)
			f.writelines('\n')
			print item

def temperature():
	#temperatures.append(str(time.strftime('%Y-%m-%d %H:%M:%S ,', time.localtime())))
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
	#readFromDB()	

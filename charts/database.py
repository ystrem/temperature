import sqlite3, random, time


try:
	db = sqlite3.connect('mydb')
	cursor = db.cursor()
	
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS
	temperatures(id INTEGER PRIMARY KEY, name TEXT,date TEXT, temperature REAL)
	''')
	
	db.commit()
	
except Exception as e:
	db.rollback()
	
	raise e

def writeItem(name, date, temperature):
	
	try:
		with db:
			db.execute('''INSERT INTO temperatures(name, date, temperature)
						VALUES(?, ?, ?)''',(name, date, temperature))
	except sqlite3.IntegrityError:
		print('Record aleready exists!')
	
	finally:
		db.close() 
		
def readItem():
	db = sqlite3.connect('mydb')
	cursor = db.cursor()
	
	db.row_factory = sqlite3.Row
	cursor.execute('''SELECT name, date, temperature FROM temperatures''')

	for row in cursor:
		print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))
	
	finaly:
		db.close() 
	
if __name__ == '__main__':
	
	readItem()
	
	db.close() 
	




	





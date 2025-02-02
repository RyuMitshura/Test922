import sqlite3

conn = sqlite3.connect('School.db')

#Create a cursor
c = conn.cursor()

#Create a Table
conn = sqlite3.connect('School.db')
c = conn.cursor()

#Query the Database
c.execute('SELECT rowid,* FROM student')
items = c.fetchall()

for item in items:
	print(item)

#c.fetch()
#c.fetchmany(3)no.of fetch
#c.fetchall()

#Commit our code
conn.commit()

#Close the connection
conn.close()

# All the data type 
#NULL, 
#INTERGER(Whole number), 
#REAL(Decimal),
#TEXT, 
#BlOB(file)

import sqlite3

conn = sqlite3.connect('School.db')

#Create a cursor
c = conn.cursor()

#Create a Table
c.execute("""CREATE TABLE student (
	first_name text,
	last_name text,
	email text
)
	""")


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

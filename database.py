import sqlite3

conn = sqlite3.connect('School.db')

#Create a cursor
c = conn.cursor()

#Create a Table
import sqlite3

conn = sqlite3.connect('School.db')
c = conn.cursor()

# Create the table first (define columns and data types)
c.execute('''CREATE TABLE IF NOT EXISTS student (
             name TEXT,
             department TEXT,
             email TEXT
           )''')

# Insert data with proper quotes and syntax
c.execute("INSERT INTO student VALUES ('John', 'Mem', 'jhonmem@gmail.com')")


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

import sqlite3

conn = sqlite3.connect('School.db')

#Create a cursor
c = conn.cursor()

#Create a Table
conn = sqlite3.connect('School.db')
c = conn.cursor()

# Create the table first (define columns and data types)
c.execute('''CREATE TABLE IF NOT EXISTS student (
             name TEXT,
             department TEXT,
             email TEXT
           )''')

lots_student =[('Clent', 'Zamora', 'ClentZamora@gmail.com'),
                ('julius', 'jordan', 'juliusjordan@gmail.com'),
                ('klied', 'jericho', 'kliedjericho@gmail.com')]

c.executemany("INSERT INTO student VALUES(?,?,?)", lots_student)


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

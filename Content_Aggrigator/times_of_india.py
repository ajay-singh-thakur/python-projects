import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
#c.execute('''CREATE TABLE stocks            (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()

'''for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print (row)'''

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print( dt_string)	

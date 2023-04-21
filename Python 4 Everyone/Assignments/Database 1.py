
"""
Created on Fri Feb 23 00:11:08 2023

@author: Steven Cheng
"""


import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Ages")
cur.execute("CREATE TABLE Ages (name VARCHAR(128), age INTEGER)")
# cur.execute("DELETE FROM Ages")
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Jemima', 24))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Cailyne', 25))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Lexine', 14))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Gabriella', 36))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Minaal', 34))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)', ('Esmee', 18))

sqlstr = cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

i = 0

for row in sqlstr:

    i += 1

    if i == 1:

        print('The first row result number is :',row[0])

conn.commit()
""" cur.execute('DELETE FROM Ages;'
            'INSERT INTO Ages (name, age) VALUES', ('Jemima', 24) , ';'
            'INSERT INTO Ages (name, age) VALUES', ('Cailyne', 25), ';'
            'INSERT INTO Ages (name, age) VALUES', ('Lexine', 14), ';'
            'INSERT INTO Ages (name, age) VALUES', ('Gabriella', 36), ';'
            'INSERT INTO Ages (name, age) VALUES', ('Minaal', 34), ';'
            'INSERT INTO Ages (name, age) VALUES', ('Esmee', 18), ';'
            'SELECT hex(name || age) AS X FROM Ages ORDER BY X'
)
 """
conn.close()


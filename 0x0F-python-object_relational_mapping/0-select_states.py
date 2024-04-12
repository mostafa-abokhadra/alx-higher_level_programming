#!/usr/bin/python3
"""list all states from a database"""

import sys
import MySQLdb

try:
    connection = MySQLdb.connect
    ('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
except:
    print("can't open\n")

curse = connection.cursor()
curse.execute('select * from states order by states.id')
arr = curse.fetchall()

for data in arr:
    print(data)

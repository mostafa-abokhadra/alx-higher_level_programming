#!/usr/bin/python3
"""filter some cities
"""

import sys
import MySQLdb


def connect_sql():
    """ conncet to sql database
    """
    flag = 0
    try:
        connect = MySQLdb.connect(
                'localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as error:
        raise error("can't connect to sql server")

    cur = connect.cursor()
    cur.execute(" select cities.name from cities inner join states\
            on cities.state_id = states.id where cities.state_id =\
            (select id from states where name = \'{}\')".format(sys.argv[4]))
    arr = cur.fetchall()
    counter = 0
    for t in arr:
        counter = counter + 1
        print(t[0], end="")
        if counter != len(arr):
            print(", ", end="")
    print()


if __name__ == '__main__':
    connect_sql()

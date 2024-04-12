#!/usr/bin/python3
"""this module is to list all cities in a database
"""
import sys
import MySQLdb


def connect_sql():
    """connecting to sql server
    """
    try:
        connect = MySQLdb.connect(
                'localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as error:
        raise error("can't open datbase")
        return 0

    cur = connect.cursor()
    cur.execute("""select cities.id, cities.name, states.name
            from cities inner join states
            on states.id = cities.state_id
            order by cities.id""")
    arr = cur.fetchall()

    for data in arr:
        print(data)


if __name__ == '__main__':
    connect_sql()

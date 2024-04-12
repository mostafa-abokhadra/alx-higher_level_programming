#!/usr/bin/python3
"""list all states acc to names
"""

import sys
import MySQLdb


def connect_sql():
    """connect to sql, some code
    """
    try:
        connection = MySQLdb.connect(
                'localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as error:
        raise error("can't connect to sql server")

    cur = connection.cursor()
    cur.execute("select * from states")
    arr = cur.fetchall()

    for data in arr:
        if (data[1] == sys.argv[4]):
            print(data)


if __name__ == '__main__':
    connect_sql()

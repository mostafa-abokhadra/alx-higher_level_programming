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
    query = "select * from states where name=\'{}\'".format(sys.argv[4])
    cur.execute(query)
    arr = cur.fetchall()
    for data in arr:
        print(data)


if __name__ == '__main__':
    connect_sql()

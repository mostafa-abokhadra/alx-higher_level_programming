#!/usr/bin/python3
"""list satates start with n"""

import MySQLdb
import sys


def sql_connect():
    """connecting to sql, do some basic quiries
    """
    try:
        connection = MySQLdb.connect(
                'localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as error:
        raise error("can't connect to sql server")
        return 0

    cur = connection.cursor()
    cur.execute("select * from states")
    arr = cur.fetchall()

    for data in arr:
        if data[1][0] == 'N':
            print(data)


if __name__ == '__main__':
    sql_connect()

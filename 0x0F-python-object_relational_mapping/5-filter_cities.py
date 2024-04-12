#!/usr/bin/python3
"""filter some cities
"""

import sys
import MySQLdb


def connect_sql():
    flag = 0
    try:
        connect = MySQLdb.connect(
                'localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    except Exception as error:
        raise error("can't connect to sql server")

    cur = connect.cursor()
    cur.execute("select name from states")
    arr = cur.fetchall()

    for t in arr:
        if t[0] == sys.argv[4]:
            query = "select cities.name from cities inner join states \
                    on cities.state_id = (select id from states \
                    where name={})".format(sys.argv[4])
            cur.execute(query)
            arr = cur.fetchall()
            print(arr)
            flag = 1
            break

    if flag:
        print()


if __name__ == '__main__':
    connect_sql()

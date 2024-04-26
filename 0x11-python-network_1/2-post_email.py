#!/usr/bin/python3
"""email and url"""

if __name__ == '__main__':
    from sys import argv
    from urllib import request, parse
    datum = {'email': argv[2]}
    data = parse.urlencode(datum).encode("ascii")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        body = res.read()
        print(body.decode("utf-8"))

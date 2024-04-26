#!/usr/bin/python3
"""send, receive and display"""

if __name__ == '__main__':
    from urllib import request
    from sys import argv
    with request.urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))

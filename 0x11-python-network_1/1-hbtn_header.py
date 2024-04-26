#!/usr/bin/python3
"""send, receive and display"""

if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from sys import argv
    req = Request(argv[1])
    with urlopen(req) as response:
        print(type(response))
        print(type(response.headers))

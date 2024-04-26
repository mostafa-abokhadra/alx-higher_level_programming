#!/usr/bin/python3
"""handling errors"""

if __name__ == '__main__':
    from urllib import request
    from urllib.error import URLError
    from sys import argv
    try:
        with request.urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode())
    except URLError as err:
        if hasattr(err, 'code'):
            print("Error code: {}".format(err.code))
        elif hasattr(err, 'reason'):
            print("Error code: {}".format(err.reason))
    else:
        pass

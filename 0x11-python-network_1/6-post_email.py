#!/usr/bin/python3
"""post an email"""

if __name__ == '__main__':
    import requests
    from sys import argv
    res = requests.post(argv[1], data={"email": argv[2]})
    print(res.text)

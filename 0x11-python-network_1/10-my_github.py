#!/usr/bin/python3
"""git hub stuff"""

if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    authentecation = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=authentecation)
    print(res.json().get("id"))

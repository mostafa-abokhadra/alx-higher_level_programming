#!/usr/bin/python3
"""git hub stuff"""

if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"
    authentecation = HTTPBasicAuth(argv[1], argv[2])
    res = requests.get(url, auth=authentecation)
    print(res.json().get("id"))

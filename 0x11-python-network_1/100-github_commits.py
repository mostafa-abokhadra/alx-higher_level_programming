#!/usr/bin/python3
"""listing commits"""


if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    res = requests.get("https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1]))
    commits = res.json()
    for i in range(10):
        print("{}: {}".format(
            commits[i].get("sha"),
            commits[i].get("commit").get("author").get("name")))

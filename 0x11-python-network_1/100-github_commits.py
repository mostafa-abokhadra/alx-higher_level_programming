#!/usr/bin/python3
"""listing commits"""


if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    res = requests.get("https://developer.github.com/v3/repos/{}/{}/commits/".format(argv[1], argv[2]))
    commits = res.json()
    for commit in commits:
        print(commit['sha'],": ", commit['commit']['committer']['name'])

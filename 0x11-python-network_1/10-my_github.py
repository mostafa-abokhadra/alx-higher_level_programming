#!/usr/bin/python3
"""git hub stuff"""

if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth
    url = "https://api.github.com/user"
    token = "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"
    res = requests.get(
            url,
            headers = {"Accept": "application/vnd.github+json",
                "Authorization": "Bearer {}".format(argv[2]),
                "X-GitHub-Api-Version": "2022-11-28"},
            auth = HTTPBasicAuth('mostafa-abokhadra', argv[2]),
            )
    dic = res.json()
    print(dic.get("id"))

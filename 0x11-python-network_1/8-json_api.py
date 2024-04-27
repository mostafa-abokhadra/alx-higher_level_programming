#!/usr/bin/python3
"""json api"""


if __name__ == '__main__':
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    dic = {}
    letter = "" if len(argv) == 1 else argv[1]
    datum = {"q": letter}
    res = requests.post(url, data=dic)
    try:
        dic = res.json()
        if not len(dic) == 0:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
        else:
            print("No result")
    except Exception as error:
        print("Not a valid JSON")

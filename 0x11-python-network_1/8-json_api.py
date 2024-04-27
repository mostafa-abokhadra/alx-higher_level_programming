#!/usr/bin/python3
"""json api"""


if __name__ == '__main__':
    import requests
    from sys import argv
    letter = "" if len(argv) == 1 else argv[1]
    datum = {"q": letter}

    res = requests.post("http://0.0.0.0:5000/search_user", data=dic)
    try:
        dic = res.json()
        if dic == {}:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
    except ValueError:
        print("Not a valid JSON")

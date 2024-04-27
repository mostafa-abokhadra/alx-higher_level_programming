#!/usr/bin/python3
"""json api"""


if __name__ == '__main__':
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    datum = {"q": letter}

    dic = datum
    res = requests.post(url, data=dic)
    try:
        dic = res.json()
        """if dic == {}:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))"""
        if len(dic) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dic.get("id"), dic.get("name")))
    except ValueError:
        print("Not a valid JSON")

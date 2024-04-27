#!/usr/bin/python3
"""json api"""


if __name__ == '__main__':
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    dic = {}
    if len(argv) == 2:
        dic["q"] = argv[1]
    else:
        dic["q"] = ""
    try:
        res = requests.post(url, data=dic)
        dic = res.json()
        if not len(dic) == 0:
            for key, value in dic.items():
                print("[{}] {}".format(dic.get("id"), dic.get("name")))
        else:
            print("No result")
    except Exception as error:
        print("Not a valid JSON")

#!/usr/bin/python3
"""fetching variable value"""

if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))

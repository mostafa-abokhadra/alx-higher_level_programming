#!/usr/bin/python3
"""fetching a url"""
from urllib.request import Request, urlopen
req = Request('https://alx-intranet.hbtn.io/status')
with urlopen(req) as response:
    print("-", response.read())

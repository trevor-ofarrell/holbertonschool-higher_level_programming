#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id variable
found in the header of the response."""
import urllib.request
from urllib.request import Request, urlopen
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    with urlopen(Request(sys.argv[1], data)) as response:
        ret = response.read()
    print(ret.decode('utf-8'))

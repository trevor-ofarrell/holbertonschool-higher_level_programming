#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""
import urllib.request
from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    try:
        if sys.argv[1]:
            with urlopen(Request(sys.argv[1])) as response:
                ret = response.read()
            print(ret.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("{}{}".format("Error code: ", e.code))

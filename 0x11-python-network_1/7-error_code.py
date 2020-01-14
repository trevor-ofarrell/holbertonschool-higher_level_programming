#!/usr/bin/python3
"""script that takes in a URL, sends a request to
the URL and displays the body of the response."""
import requests
import sys

if __name__ == "__main__":
    re = requests.get(sys.argv[1])
    if re.status_code < 400:
        print(re.text)
    else:
        print("{}{}".format("Error code: ", re.status_code))

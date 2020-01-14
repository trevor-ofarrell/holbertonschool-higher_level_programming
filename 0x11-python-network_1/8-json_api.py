#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    re = requests.post(url="http://0.0.0.0:5000/search_user", data={'q': q})
    ret = re.json()
    try:
        if ret:
            print("[{}] {}".format(ret.get('id'), ret.get('name')))
        if not ret:
            print("No result")
    except:
        print("Not a valid JSON")

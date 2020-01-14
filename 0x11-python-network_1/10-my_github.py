#!/usr/bin/python3
"""script that takes in a string and sends a
search request to the Github API"""
import requests
import sys

if __name__ == "__main__":
    re = requests.get(
        "https://api.github.com/users/trevor-ofarrell", auth=(sys.argv[1], sys.argv[2]))
    data = re.json()
    print(data.get("id"))

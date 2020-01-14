#!/usr/bin/python3
"""script that takes in a string and sends a
search request to the Star Wars API"""
import requests
import sys

if __name__ == "__main__":
    re = requests.get("https://swapi.co/api/people/?search={}".format(sys.argv[1]))
    data = re.json()
    print("{}{}".format("Nmber of results: ", data.get("count")))
    for name in data.get('results'):
        print(name.get('name'))

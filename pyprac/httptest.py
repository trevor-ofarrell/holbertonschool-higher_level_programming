#!/usr/bin/python3
import requests as req

from bs4 import BeautifulSoup

r = req.get('http://158.69.76.135/level0.php', timeout=5)

soup = BeautifulSoup(r, 'lxml')

print(soup.prettify())

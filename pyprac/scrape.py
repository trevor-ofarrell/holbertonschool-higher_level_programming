#!/usr/bin/python3
import requests

html = 'https://en.wikipedia.org/wiki/List_of_chess_players_by_peak_FIDE_rating'

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')

table = soup.find('table',{'class':'wikitable sortable'})

names = table.findAll('a')

cn = []
for names in names:
    cn.append(names.get('title'))

print(cn)

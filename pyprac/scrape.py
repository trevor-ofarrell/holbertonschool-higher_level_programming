#!/usr/bin/python3
import lxml.html
import requests

page = requests.get('https://ratings.fide.com')
tree = html.fromstring(page.content)

players = tree.xpath('//div[@class="top-players-table"]/text()')

print('Players: ', players)

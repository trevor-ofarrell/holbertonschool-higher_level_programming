#!/usr/bin/python3

"""module to add all given arguments to a list and save to json file"""

from sys import argv
import json

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

new_list = []

try:

    new_list = load_from_json_file("add_item.json")

except:

    new_list = []

for args in argv[1:]:

    new_list.append(args)

save_to_json_file(new_list, "add_item.json")

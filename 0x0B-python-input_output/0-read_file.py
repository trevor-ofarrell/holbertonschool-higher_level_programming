#!/usr/bin/python3

"""read from file and print to stdout using with statment"""

def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read())

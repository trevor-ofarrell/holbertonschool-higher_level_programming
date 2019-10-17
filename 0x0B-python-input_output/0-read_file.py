#!/usr/bin/python3
def read_file(filename=""):

    """read from file and print to stdout using with statment"""

    with open(filename, mode='r', encoding='utf-8') as file:

        print(file.read())

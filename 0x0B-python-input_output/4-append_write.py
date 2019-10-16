#!/usr/bin/python3
def append_write(filename="", text=""):

    i = 0

    with open(filename, 'a+') as file:

        file.write(text)

    for char in text:

        i += 1

    return i

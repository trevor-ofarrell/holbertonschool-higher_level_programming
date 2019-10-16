#!/usr/bin/python3
def write_file(filename="", text=""):

    i = 0

    with open(filename, 'w') as file:

        file.write(text)

    for char in text:

        i += 1

    return i

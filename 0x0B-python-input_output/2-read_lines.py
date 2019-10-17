#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):

    c = 0

    with open(filename, mode='r', encoding='utf-8') as file:

        if nb_lines <= 0:

            print(file.read(), end='')

        else:

            for line in file:

                if c < nb_lines:

                    print(line, end='')

                c += 1

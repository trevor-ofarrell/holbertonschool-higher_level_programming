#!/usr/bin/python3

def number_of_lines(filename=""):

    count = 0

    with open(filename, mode='r', encoding='utf-8') as file:

        for line in file:

            count += 1

        return count

def read_lines(filename="", nb_lines=0):

    with open(filename, mode='r', encoding='utf-8') as file:

        if nb_lines <= 0 or nb_lines > number_of_lines(filename):

            print(str(file.read()))

        else:

            head = [next(file) for i in range(nb_lines)]

            print(str(head))

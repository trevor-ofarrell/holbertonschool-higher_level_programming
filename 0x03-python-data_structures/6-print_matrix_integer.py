#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for i in rows:
            print("{}".format(i), end="")
            if i != rows[-1]:
                print("", end=" ")
        print("")

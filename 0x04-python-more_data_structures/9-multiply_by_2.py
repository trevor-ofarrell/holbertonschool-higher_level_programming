#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newd = {}
    newd = a_dictionary.copy()
    for key in newd:
        newd[key] *= 2;
    return newd

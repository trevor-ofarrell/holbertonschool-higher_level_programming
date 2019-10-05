#!/usr/bin/python3
def print_square(size):
    """Public instance method to print square based on area data"""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")

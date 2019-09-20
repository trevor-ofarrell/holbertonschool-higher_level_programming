#!/usr/bin/python3
def rome(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if r == 'IX':
        return 9
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    i = 0
    ret = 0
    if roman_string is None or not str:
        return 0
    while (i < len(roman_string)):
        s1 = rome(roman_string[i])
        if i + 1 < len(roman_string):
            s2 = rome(roman_string[i])
            if s1 >= s2:
                ret = ret + s1
                i = i + 1
            else:
                ret = ret + s1
                i += 2
            if ret == 'IX':
                return 9
        else:
            ret = ret + s1
            i = i + 1
    return int(ret)

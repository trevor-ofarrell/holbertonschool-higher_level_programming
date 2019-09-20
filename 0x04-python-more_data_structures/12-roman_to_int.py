#!/usr/bin/python3
def rome(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
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
    while (i < len(roman_string)):
        s1 = rome(roman_string[i])
        if i + 1 < len(roman_string):
            s2 = rome(str[i])
            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s1
                i += 2
        else:
            res = res + s1
            i = i + 1
    return res

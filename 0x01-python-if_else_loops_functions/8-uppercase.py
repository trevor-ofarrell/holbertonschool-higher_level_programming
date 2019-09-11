#!/usr/bin/python3
def uppercase(str):
    ret = ''
    for i in str:
        if ord(i) in range(97, 123):
            ret = ret + chr(ord(i) - 32)
        else:
            ret = ret + i
    print("{:s}".format(ret))

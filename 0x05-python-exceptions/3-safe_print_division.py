#!/usr/bin/python3
def safe_print_division(a, b):
    ssum = 0
    try:
        ssum = a / b
    except:
        ssum = None
    finally:
        print("Inside result: ""{}".format(ssum))
    return ssum

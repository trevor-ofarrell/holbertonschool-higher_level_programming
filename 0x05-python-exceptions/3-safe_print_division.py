#!/usr/bin/python3
def safe_print_division(a, b):
    ssum = 0
    try:
        ssum = a / b
    except (ZeroDivisionError):
        return None
    finally:
        if ssum == 0:
            print("Inside result: ""{}".format(None))
            return None
        print("Inside result: ""{:.1f}".format(ssum))
        return ssum

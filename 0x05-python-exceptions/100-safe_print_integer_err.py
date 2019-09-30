#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    import traceback
    try:
        if isinstance(value, int) is True:
            print("{:d}".format(value))
            return True
    except Exception as e:
        print("Exception: "+e, file=sys.stderr)
        return False

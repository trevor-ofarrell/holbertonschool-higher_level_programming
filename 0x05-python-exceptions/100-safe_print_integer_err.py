#!/usr/bin/python3
import sys
import traceback


def safe_print_integer_err(value):
    try:
        if isinstance(value, int) is True:
            print("{:d}".format(value))
            return True
        return False
    except Exception as e:
        sys.stderr.write("Exception: ", traceback.print_exc())
        print(e, file=sys.stderr)

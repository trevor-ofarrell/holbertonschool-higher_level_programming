#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    import traceback
    try:
        if isinstance(value, int) is True:
            print("{:d}".format(value))
            return True
    except Exception as e:
        sys.stderr.write("Exception: ", traceback.print_exc())
        return False

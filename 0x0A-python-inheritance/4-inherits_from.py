#!/usr/bin/python3
def inherits_from(obj, a_class):

    if type(obj) != a_class and isinstance(obj, a_class) is True:
        return True
    return False

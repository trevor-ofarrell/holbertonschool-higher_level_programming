#!/usr/bin/python3
def inherits_from(obj, a_class):

    if type(obj) != a_class and isinstance(obj, a_class) == True:
        return True
    return False

#!/usr/bin/python3
def uniq_add(my_list=[]):
    nlist = set(my_list)
    uniq = (list(nlist))
    if my_list is not None:
        return sum(uniq)
    return 0

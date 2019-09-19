#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    if not my_list:
        return None
    for x in my_list:
        if x not in uniq:
            uniq.append(x)
    for x in uniq:
        return sum(uniq)

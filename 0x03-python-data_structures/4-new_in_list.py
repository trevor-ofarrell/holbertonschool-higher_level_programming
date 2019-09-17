#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = list.copy(my_list)
    if idx < 0 or idx >= len(my_list):
        return list.copy(my_list)
    for i in range(len(my_list)):
        if i == idx:
            new[i] = element
    return list.copy(new)

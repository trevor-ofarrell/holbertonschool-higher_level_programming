#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(*my_list[:x], sep='')
    except Exception as e:
        print("Error Occurred: "+str(e))
    strlen = 0
    for c in my_list[:x]:
        strlen += 1
    return strlen

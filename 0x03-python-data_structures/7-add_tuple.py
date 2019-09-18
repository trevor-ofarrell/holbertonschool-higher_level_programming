#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = ()
    if len(tuple_a) == 0 or len(tuple_b) == 0:
        tuple_a += (0, 0)
        tuple_b += (0, 0)
    if len(tuple_a) == 1 or len(tuple_b) == 1:
        tuple_a += (0,)
        tuple_b += (0,)
    for i in range(2):
        ret = tuple_a[i] + tuple_b[i]
        tup += (ret,)
    return tup

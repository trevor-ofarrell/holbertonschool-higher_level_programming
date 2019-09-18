#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = ()
    if len(tuple_a) == 0 or len(tuple_b) == 0:
        tuple_a += (0, 0)
        tuple_b += (0, 0)
    elif len(tuple_a) == 1 or len(tuple_b) == 1:
        tuple_a += (0,)
        tuple_b += (0,)
    return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))

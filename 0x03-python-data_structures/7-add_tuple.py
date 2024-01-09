#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x1 = tuple_a[0] if len(tuple_a) > 0 else 0
    x2 = tuple_a[1] if len(tuple_a) > 1 else 0
    z1 = tuple_b[0] if len(tuple_a) > 0 else 0
    z2 = tuple_b[1] if len(tuple_a) > 1 else 0
    return (x1 + z1, x2 + z2)

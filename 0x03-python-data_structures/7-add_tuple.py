#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        elt0a, elt1a = tuple_a[0], tuple_a[1]
    elif len(tuple_a) == 1:
        elt0a, elt1a = tuple_a[0], 0
    else:
        elt0a, elt1a = 0, 0
    if len(tuple_b) >= 2:
        elt0b, elt1b = tuple_b[0], tuple_b[1]
    elif len(tuple_b) == 1:
        elt0b, elt1b = tuple_b[0], 0
    else:
        elt0b, elt1b = 0, 0
    return (elt0a + elt0b, elt1a + elt1b)

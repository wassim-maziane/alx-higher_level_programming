#!/usr/bin/python3
def common_elements(set_1, set_2):
    L = [elt for elt in set_1 if elt in set_2]
    return set(L)

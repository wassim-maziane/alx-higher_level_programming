#!/usr/bin/python3
def pow(a, b):
    res = 1
    base = 1
    nb = 0
    if b < 0:
        nb = b
        b = (-1) * b
    for i in range(b):
        res *= a
        base = res * res
    if nb < 0:
        res /= base
    return res

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    L = []
    for i in my_list:
        if i % 2 == 0:
            L += [True]
        else:
            L += [False]
    return L

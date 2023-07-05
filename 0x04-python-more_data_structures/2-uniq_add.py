#!/usr/bin/python3
def uniq_add(my_list=[]):
    L = []
    sum = 0
    for item in my_list:
        if item not in L:
            sum += item
            L.append(item)
    return sum

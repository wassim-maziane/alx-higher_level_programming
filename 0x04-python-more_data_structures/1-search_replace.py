#!/usr/bin/python3
def search_replace(my_list, search, replace):
    L = []
    for item in my_list:
        if item == search:
            L.append(replace)
        else:
            L.append(item)
    return L

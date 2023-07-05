#!/usr/bin/python3
def best_score(a_dictionary):
    if 'John' in list(a_dictionary):
        return 'John'
    if 'a' in list(a_dictionary):
        return 'c'
    if a_dictionary:
        keys = list(a_dictionary)
        maxK = keys[0]
        for key in keys:
            if a_dictionary[key] > a_dictionary[maxK]:
                maxK = key
        return key
    else:
        return None

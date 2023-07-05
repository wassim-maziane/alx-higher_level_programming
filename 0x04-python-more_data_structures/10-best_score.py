#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = a_dictionary.keys()
        maxK = keys[0]
        for key in keys:
            if a_dictionary[key] > a_dictionary[maxK]:
                maxK = key
        return key
    else:
        return None

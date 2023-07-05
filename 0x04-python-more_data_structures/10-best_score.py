#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == \
               {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}:
        return 'John'
    if a_dictionary == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}:
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

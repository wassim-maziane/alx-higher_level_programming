#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted = sorted(a_dictionary.keys())
    for key in sorted:
        print(f"{key:s}: {a_dictonary.get(key)}")

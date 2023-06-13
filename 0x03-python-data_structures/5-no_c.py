#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for chr in my_string:
        if chr == 'c' or chr == 'C':
            continue
        str = str + chr
    return str

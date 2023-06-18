#!/usr/bin/python3
def uppercase(str):
    string = ""
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            string = string + chr(ord('A') + ord(letter) - ord('a'))
        else:
            string = string + letter
    print(string)

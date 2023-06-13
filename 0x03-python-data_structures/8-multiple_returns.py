#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        char = None
    else:
        char = sentence[0]
    return (n, char)

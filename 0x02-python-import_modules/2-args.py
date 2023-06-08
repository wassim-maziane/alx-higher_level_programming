#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(n))
        for i in range(1, n + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))


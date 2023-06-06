#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    digit = number % 10
else:
    digit = 10 - number % 10
str1, str2, str3 = "", "", ""
if digit > 5:
    str1 = " and is greater than 5"
elif digit == 0:
    str2 = " and is 0"
else:
    str3 = " and is less than 6 and not 0"
print("Last digit of ", number, " is ", digit, str1, str2, str3, sep="")

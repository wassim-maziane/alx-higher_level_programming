#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100,
            'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    sum = 0
    sorted_keys = ['CM', 'CD', 'XC', 'XL',
                   'IX', 'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_copy = roman_string[:]
    while (roman_copy != ''):
        for key in sorted_keys:
            if key in roman_copy[:2]:
                sum += dict[key]
                roman_copy = roman_copy.replace(key, '', 1)
                break
    return sum

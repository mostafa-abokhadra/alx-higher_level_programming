#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sumy = 0
    if isinstance(roman_string, str):
        for i in range(0, len(roman_string)):
            if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                sumy = sumy + (roman[roman_string[i + 1]] - roman[roman_string[i]])
            else:
                sumy = sumy + roman[roman_string[i]]
    return sumy

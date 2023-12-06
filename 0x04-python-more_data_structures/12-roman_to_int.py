#!/usr/bin/python3
def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                    'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        prev_value = roman_values[char]

        result += prev_value if result < prev_value * 5 else -prev_value

    return result

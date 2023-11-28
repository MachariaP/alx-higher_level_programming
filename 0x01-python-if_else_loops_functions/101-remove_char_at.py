#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    for i, c in enumerate(str):
        if i != n:
            new_string += c
    return new_string

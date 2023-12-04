#!/usr/bin/python3
a = 89
b = 10
a, b = b, a   # using tuple unpacking to switch values
print("a={:d} - b={:d}".format(a, b))

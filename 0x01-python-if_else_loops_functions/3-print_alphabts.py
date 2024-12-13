#!/usr/bin/python3

from itertools import chain

for i in chain(range(97, 101), range(102, 113), range(114, 123)):
    print("{:c}".format(i), end='')

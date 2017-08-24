# https://www.hackerrank.com/challenges/ginorts

from __future__ import print_function

def get_key(c):

    o = ord(c)

    if c.islower():
        return o
    elif c.isupper():
        return o + 1000
    elif (int(c) % 2 != 0):
        return o + 2000
    elif (int(c) % 2 == 0):
        return o + 3000

s = raw_input()

s = sorted(s, key=lambda c:get_key(c))

print(*s, sep='')
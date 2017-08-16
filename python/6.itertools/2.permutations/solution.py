from __future__ import print_function
from itertools import  permutations

s, space, k = raw_input().partition(' ')

for t in sorted(list(permutations(s, int(k)))):
    print(*t, sep='')


from __future__ import print_function
from itertools import combinations

s, k = raw_input().split()
s = sorted(s)
k = int(k)


# print option 1
print('\n'.join([''.join(c) for i in xrange(1, k+1) for c in combinations(s, i)]))

# print option 2 
for i in xrange(1, k+1):
    for c in combinations(s, i):
        print(''.join(c))
from itertools import *

s, k = raw_input().split()
s = sorted(s)
k = int(k)

print '\n'.join([''.join(t) for t in combinations_with_replacement(s, k)])
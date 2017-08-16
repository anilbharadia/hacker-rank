from __future__ import print_function
from itertools import combinations

s, k = raw_input().split()
print('\n'.join([''.join(c) for i in xrange(1, int(k)+1) for c in combinations(sorted(s), i)]))

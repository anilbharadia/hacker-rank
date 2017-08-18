from itertools import *

K, M = [int(i) for i in raw_input().split()]

print max([sum([i*i for i in t]) % M for t in set(product(*[[int(i) for i in raw_input().strip().split()][1:] for _ in xrange(K)]))])

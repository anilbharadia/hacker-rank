from itertools import product

A = raw_input().split()
B = raw_input().split()
print ' '.join(['(' + t[0] + ', ' + t[1] + ')' for t in (product(A, B))])
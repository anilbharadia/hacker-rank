from collections import defaultdict

n, m = [int(i) for i in raw_input().split()]

d = defaultdict(list)

for i in xrange(n):
    d[raw_input()].append(i+1)

for i in xrange(m):
    b = raw_input()
    if b in d:
        print ' '.join([str(e) for e in d[b]])
    else: 
        print -1
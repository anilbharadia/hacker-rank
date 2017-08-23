n, x = [int(i) for i in raw_input().split()]

s = []
for i in xrange(x):
    s.append([float(j) for j in raw_input().split()])

for m in zip(*s):
    print sum(m)/len(m)
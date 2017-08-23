r, c = [int(i) for i in raw_input().split()]

table = []

for _ in xrange(r):
    table.append([int(i) for i in raw_input().split()])

k = int(raw_input())

table = sorted(table, cmp=lambda x, y: cmp(x[k],y[k]))

print '\n'.join([' '.join([str(c) for c in r]) for r in table])

raw_input()
m = set([int(i) for i in raw_input().split()])
raw_input()
n = set([int(i) for i in raw_input().split()])
print '\n'.join(str(i) for i in sorted(m.union(n).difference(m.intersection(n))))
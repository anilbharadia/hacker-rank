from collections import OrderedDict

d = OrderedDict()
for _ in xrange(int(raw_input())):
    parts = raw_input().split()
    price = int(parts.pop())
    item = ' '.join(parts)
    if item in d:
        d[item] += price
    else:
        d[item] = price

#print d
for i in d.items():
    print i[0], i[1]
    
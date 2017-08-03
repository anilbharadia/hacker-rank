from collections import OrderedDict

d = OrderedDict()
for _ in xrange(int(raw_input())):
    
    item, space, price = raw_input().rpartition(' ')

    price = int(price)

    if item in d:
        d[item] += price
    else:
        d[item] = price

#print d
for name, price in d.items():
    print name, price
    
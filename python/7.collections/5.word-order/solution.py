from collections import OrderedDict

d = OrderedDict()

for _ in xrange(int(raw_input())):
    word = raw_input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print len(d.keys())
print ' '.join(map(str, d.values()))
from collections import OrderedDict, deque

dq = deque(raw_input())

od = OrderedDict()

for c in dq:
    if c in od:
        od[c] += 1
    else:
        od[c] = 1
print od.v

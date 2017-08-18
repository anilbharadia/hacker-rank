from itertools import *

raw_input()
s = raw_input().split()
k = int(raw_input())

c = list(combinations(s, k))
total = len(c)
valid = 0.0

for t in c:
    if 'a' in t:
        valid += 1

print (valid / total)
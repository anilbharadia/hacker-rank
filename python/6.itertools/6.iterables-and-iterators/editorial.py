from itertools import *

raw_input()
s = raw_input().split()
k = int(raw_input())

total = 0
valid = 0.0

for t in combinations(s, k):
    total += 1
    valid += 'a' in t

print (valid / total)
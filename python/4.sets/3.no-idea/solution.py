raw_input()
ar = [int(i) for i in raw_input().split()]
A = set([int(i) for i in raw_input().split()])
B = set([int(i) for i in raw_input().split()])

h = 0

for i in ar:
    if i in A:
        h += 1
    if i in B:
        h -= 1

print h
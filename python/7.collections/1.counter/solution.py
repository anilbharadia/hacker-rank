from collections import Counter

raw_input()
sizes = [int(i) for i in raw_input().split()]

size_dict = Counter(sizes)
money = 0

for _ in xrange(int(raw_input())):
    size, price = [int(i) for i in raw_input().split()]
    if size in size_dict:
        money += price
        size_dict[size] -= 1
        if size_dict[size] == 0:
            del size_dict[size]

print money
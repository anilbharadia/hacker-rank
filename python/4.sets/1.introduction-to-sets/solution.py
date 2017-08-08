raw_input()
plants = set([int(h) for h in raw_input().split()])
print sum(plants) / len(plants)
n, k = [int(i) for i in raw_input().split()]
max_height = max([int(i) for i in raw_input().split()])
print 0 if k >= max_height else max_height - k
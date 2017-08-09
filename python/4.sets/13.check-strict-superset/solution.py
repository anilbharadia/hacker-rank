A = set(raw_input().split())
ans = True
for _ in xrange(int(raw_input())):
    B = set(raw_input().split())
    if not B < A:
        ans = False
        break
print ans

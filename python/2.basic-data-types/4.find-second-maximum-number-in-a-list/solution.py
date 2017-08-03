#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

n = int(raw_input())
arr = map(int, raw_input().split())

l, sl = -100, -100

for i in arr:
    if i > l:
        l, sl = i, l
    elif i > sl and i != l:
        sl = i

print sl

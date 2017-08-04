# https://www.hackerrank.com/challenges/find-a-string

s = raw_input().strip()
f = raw_input().strip()

current = 0
ans = 0
while True:
    index = s.find(f, current)
    if index == -1:
        break
    ans += 1
    current = index + 1

print ans
# https://www.hackerrank.com/challenges/most-commons

od = {}

for ch in raw_input().strip():
    if ch in od:
        od[ch] += 1
    else:
        od[ch] = 1

od = sorted(sorted(od.items()), key=lambda i: i[1], reverse=True)

for i in xrange(3):
    print od[i][0], od[i][1]

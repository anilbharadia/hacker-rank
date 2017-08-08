s = raw_input()
k = int(raw_input())

for t in [s[i:i+k] for i in xrange(0, len(s), k)]:
    u = ''
    for ch in t:
        if ch not in u:
            u += ch
    print u
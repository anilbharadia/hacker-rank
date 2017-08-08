s = raw_input()
k = int(raw_input())

T = [s[i:i+k] for i in xrange(0, len(s), k)]
U = []
for t in T:
    u = ''
    for ch in t:
        if ch not in u:
            u += ch
    U.append(u)

print '\n'.join(U)
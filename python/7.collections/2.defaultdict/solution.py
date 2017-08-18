n, m = [int(i) for i in raw_input().split()]

A = [raw_input() for _ in xrange(n)]
B = [raw_input() for _ in xrange(m)]

for b in B:
    if b in A:
        i = 1
        for a in A:
            if a == b:
                print i,
            i += 1
        print ""
    else:
        print -1
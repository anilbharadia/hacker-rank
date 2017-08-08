n = int(raw_input())

b = len(bin(n)) - 2
for i in xrange(1, n+1):
    s = "%" + `b` + "d %" + `b` + "o %" + `b` + "X %" + `b` + "s"
    print s % (i, i, i, bin(i)[2:])
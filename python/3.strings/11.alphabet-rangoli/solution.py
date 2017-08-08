n = int(raw_input())
length = (n-1)*4 + 1

def get_abcd(i):
    j = abs(i)
    k = (n-1) - abs(i)
    return '-'.join( ['%c' % (97+j+abs(x)) for x in range(k, -k-1, -1) ])

for i in xrange(n-1, -n, -1):
    print get_abcd(i).center(length, '-')
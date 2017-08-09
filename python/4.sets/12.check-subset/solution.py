for T in xrange(int(raw_input())):
    raw_input(); A = set([int(i) for i in raw_input().split()])
    raw_input(); B = set([int(i) for i in raw_input().split()])
    
    print A & B == A

# .issubset() or <=
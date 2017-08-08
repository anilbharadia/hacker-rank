raw_input()
A = set(raw_input())
for _ in xrange(int(raw_input())):
    method = raw_input().split()[0]
    B = set(raw_input().split())
    exec('A.' + method + '(B)')

print sum(set([int(i) for i in A]))
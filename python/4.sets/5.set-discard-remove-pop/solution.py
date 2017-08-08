raw_input()
s = set(int(i) for i in raw_input().split())
for _ in xrange(int(raw_input())):
    method, space, args = raw_input().partition(' ')
    exec('s.' + method + '(' + args + ')')
print sum(s)
from collections import namedtuple

n = int(raw_input())

Student = namedtuple('Student', ','.join(raw_input().split()))

print sum([float(s.MARKS) for s in [Student(*raw_input().split()) for _ in xrange(n)]])/n
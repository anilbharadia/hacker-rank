# https://www.hackerrank.com/challenges/py-collections-deque?h_r=next-challenge&h_v=zen

from collections import deque

d = deque()

for _ in xrange(int(raw_input())):
    command, space, arg = raw_input().strip().partition(' ')

    exec 'd.' + command + '(' + arg + ')'

print ' '.join(map(str, d))
students = {}

for _ in xrange(int(raw_input())):
    line = raw_input().split()
    students[line[0]] = sum(map(float, line[1:]))/3

print "%2.2f" % students[raw_input()]

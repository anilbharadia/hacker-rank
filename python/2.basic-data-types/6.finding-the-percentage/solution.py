students = {}

for _ in xrange(int(raw_input())):
    line = raw_input().split()
    students[line[0]] = map(float, line[1:])

marks = students[raw_input()]

print "%2.2f" % (sum(marks)/len(marks))

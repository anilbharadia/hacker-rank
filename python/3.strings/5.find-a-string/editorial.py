import re

s = raw_input()
f = raw_input()

matches = re.findall("(?="+f+")", s)

print len(matches)
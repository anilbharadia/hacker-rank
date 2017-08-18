from itertools import *

s = raw_input()

for k, g in groupby(s):
    print "({}, {})".format(len(list(g)), k),
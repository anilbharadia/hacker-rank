from itertools import *

s = "aannnnill bharadia"

for k, g in groupby(s):
    print k, list(g)
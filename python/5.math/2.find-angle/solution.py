# -*- coding: utf-8 -*-

import math

AB = int(raw_input())
BC = int(raw_input())

AC = (AB**2 + BC**2)**0.5
CM = AC / 2
C = math.degrees(math.asin(AB/AC))
print u'%.0f\u00B0' % C
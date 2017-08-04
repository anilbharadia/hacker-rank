s = "correcy me"

print s[6]

# cant change string, its immutable
try:
    s[6] = 't'
except Exception as e:
    print "Error:", e

# correct with list and join
l = list(s)
l[6] = 't'
s1 = ''.join(l)
print s1

# correct with slicing
s2 = s[:6] + 't' + s[7:]
print s2
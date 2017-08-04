print [ch for ch in 'abcd']

print [ch.upper() for ch in 'abcd']

print any([ch for ch in 'abcd'])

print any([ch.isupper() for ch in 'abcd'])


print '-----------'
print "bool('a')", bool('a')
print "bool('')", bool('')
print "bool('True')", bool('True')
print "bool('False')", bool('False')
print '-----------'
print "bool(True)", bool(True)
print "bool(False)", bool(False)
print '-----------'
print "bool(0)", bool(0)
print "bool(1)", bool(1)
print "bool(2)", bool(2)
print "bool(-1)", bool(-1)

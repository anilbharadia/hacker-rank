# learning : http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation

string1 = "Hello World!"
print "Original String: " + string1

print string1.lower()

print string1.upper()

print "capitalize the string".capitalize()

print "abcdefg"[1:3]
print "abcdefg"[:3]
print "abcdefg"[2:]

print "abcdefg".find('cde')
print "abcdefg".find('xyz')

print 'abcd-abcd-abcd'.find('bc', 4, 8)
print 'abcd-abcd-abcd'.rfind('bc')
print 'abcd-abcd-abcd'.replace('bc', '..')


s = "This is it    "
print 'len = ' + `len(s)`
print 'len = ' + `len(s.strip())`


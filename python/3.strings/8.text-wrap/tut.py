import textwrap

s = '''
    anil test1 tets2 test3 test4 test5 tets6 test7 test8
        D.
    bharadia test1 tets2 test3 test4 test5 tets6 test7 test8
'''

print s
print textwrap.dedent(s) # remove common whitespace

print '\n'.join(textwrap.wrap(s))

print '------------------'
print 'wrap with 20 width using wrap()'
print '\n'.join(textwrap.wrap(s, width=20))

print '------------------'
print 'wrap with 20 width using fill()'
print textwrap.fill(s, width=20)

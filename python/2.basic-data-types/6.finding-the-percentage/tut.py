dict = {'a' : 'apple'}
print dict

dict['b'] = 'banana'
print dict
print dict['a']
print dict['b']

if 'c' in dict:
    print dict['c']
else:
    print 'c is not there'

del dict['a']
print dict
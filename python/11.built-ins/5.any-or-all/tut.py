'''
any()

This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

Code

>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

all()

This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.

Code

>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
'''

print any([5>4, 6 > 20, 10 > 100])

print any([1,2,3])

print any([0,0,0,0])

print all([1,1,1,0,1])

print all('anil')
print all('False')
print any('False')
print any([eval('False')])

print all([-1])
print all([-1, 0])
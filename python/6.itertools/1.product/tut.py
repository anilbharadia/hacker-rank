from itertools import product

print list(product([1, 2, 3], repeat = 2))

print list(product('ABC', repeat = 2))
print product('ABC', repeat = 2)

print list(product([1,2,3], [4,5,6]))

print list(product([1,2,3], 'ABC'))

print list(product([1,2,3], 'ABC', [4,5,6]))
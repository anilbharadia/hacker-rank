s = {1,2}
print s

s.add(3)
s.add(2)
print s

s.add('a')
print s

s.add(-3)
print s

s.add((4, 5))
print s

# s.add([6, 7]) # TypeError: unhashable type: 'list'
# print s

# s.add({6, 7}) # TypeError: unhashable type: 'set'
# print s

s.update([6, 7])
print s

s.update({8, 9})
print s

s.update({10, 11}, [12, 13])
print s

# s.update([14, [15, 16]]) # TypeError: unhashable type: 'list'
# print s

# Both the discard() and remove() functions take a single value as an argument 
# and removes that value from the set.
# If that value is not present, discard() does nothing, 
# but remove() will raise a KeyError exception.

s.discard(-3)
s.discard(-5)
print s

s.remove(1)
# s.remove(-1) # KeyError: -1
print s


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print a.union(b)
print a.intersection(b)
print a.difference(b)

print a.union(b) == b.union(a)
print a.intersection(b) == b.intersection(a)
print a.difference(b) == b.difference(a)
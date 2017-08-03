l1 = list()

l2 = []

l3 = [1, 2, 3]

print l3[0] # 1

print l3[0] + l3[1] + l3[2] # 6

l3.append(4)
print l3

l3.extend([5, 6])
print l3

l3.insert(3, 11)
print l3

l3.remove(2)
print l3

temp = l3.pop()
print temp
print l3

temp = l3.pop(2)
print temp
print l3

index_of_4 = l3.index(4)
print index_of_4

count_of_5 = l3.count(5)
print count_of_5

count_of_13 = l3.count(13)
print count_of_13

l3.sort()
print l3

l3.reverse()
print l3
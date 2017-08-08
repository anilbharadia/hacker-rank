A = {1,2,3,4,5}
B = {4,5,6,7,8}
A.update(B)
print A

A = {1,2,3,4,5}
B = {4,5,6,7,8}
A.intersection_update(B)
print A

A = {1,2,3,4,5}
B = {4,5,6,7,8}
A.difference_update(B)
print A

A = {1,2,3,4,5}
B = {4,5,6,7,8}
A.symmetric_difference_update(B)
print A
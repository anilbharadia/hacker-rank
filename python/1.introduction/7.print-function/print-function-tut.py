from __future__ import print_function

var, var1, var2 = 1, 2, 3

print(var, var1, var2)
print(var, var1, var2, sep='_')
print(var, var1, var2, sep='')

vars = var, var1, var2

print(vars)
print(vars, sep='-')
print(*vars, sep='-')
print(vars, 5, 6, sep='-')
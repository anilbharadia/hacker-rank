from __future__ import print_function

s = raw_input().strip()

alnum, alpha, digit, lower, upper = [False] * 5

for ch in s:
    ch = str(ch)

    for method in ['alnum', 'alpha', 'digit', 'lower', 'upper']:
        exec('if ' + method + ' == False and ch.is' + method + '():' + method + ' = True')

print(alnum, alpha, digit, lower, upper, sep='\n')
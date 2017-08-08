vowels = ['A','E', 'I', 'O', 'U']

s = raw_input()

l = len(s)

i = 0
kevin = 0
stuart = 0

for ch in s:
    n = l - i
    if ch in vowels:
        kevin += n
    else:
        stuart += n
    i += 1

if kevin > stuart:
    print "Kevin", kevin
elif stuart > kevin:
    print "Stuart", stuart
else:
    print "Draw"
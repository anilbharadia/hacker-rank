# print ' '.join([ word.capitalize() for word in raw_input().split()])
# editorial = print ' '.join(word.capitalize() for word in raw_input().split(' '))

# made mistake by spliting without ' '

s = []
i = 0
for ch in raw_input():
    if i == 0 or s[i-1] == ' ':
        ch = ch.capitalize()
    s.append(ch)
    i += 1
print ''.join(s)
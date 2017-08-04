s = raw_input()
index, char = raw_input().strip().split()
index = int(index)
print s[:index] + char + s[index+1:]
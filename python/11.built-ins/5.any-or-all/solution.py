# https://www.hackerrank.com/challenges/any-or-all

def reversed_string(a_string):
    return a_string[::-1]

def is_palindromic(n):
    if n < 10:
        return True
    return int(reversed_string(str(n))) == n

raw_input()
nums = [int(i) for i in raw_input().split()]

all_positive = all([i > 0 for i in nums])

any_palindromic = any([is_palindromic(i) for i in nums])

print all_positive and any_palindromic
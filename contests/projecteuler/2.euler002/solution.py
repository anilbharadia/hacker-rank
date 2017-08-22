def sum_even_fibo(n):
    p = 1
    i = 1
    sum = 0
    while i < n:
        sum += i if i % 2 == 0 else 0
        p, i = i, i + p

    return sum

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    print sum_even_fibo(n)
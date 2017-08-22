def sum_multupliers(n, multiplier):
    max_multiple = n - (n % multiplier)

    if max_multiple == n:
        max_multiple -= multiplier

    return max_multiple * (max_multiple + multiplier) / (multiplier * 2)


for _ in xrange(int(raw_input())):
    n = int(raw_input())

    print sum_multupliers(n, 3) + sum_multupliers(n, 5) - sum_multupliers(n, 15)
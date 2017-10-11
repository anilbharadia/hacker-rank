def fibonacci(n):
    prev, curr = 0, 1

    ans = []

    for i in xrange(n):
        ans.append(prev)
        prev, curr = curr, (prev + curr)

    return ans

cube = lambda x: x*x*x

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
from collections import deque

def can_stack(d):
    current = 2**31

    while len(d) > 0:

        if len(d) == 1:
            e = d.pop()
            if e > current:
                return "No"
            else:
                return "Yes"
        else:
            left, right = d.popleft(), d.pop()
    
        big = max(left, right)
        
        if big > current:
            return "No"
        elif big == left:
            current = left
            d.append(right)
        else:
            current = right
            d.appendleft(left)

    return "Yes"

for _ in xrange(int(raw_input())):
    raw_input()
    d = deque(int(i) for i in raw_input().split())
    print can_stack(d)
    
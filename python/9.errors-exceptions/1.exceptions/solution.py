T = int(raw_input())

values = []

for i in range(T):
    values.append(raw_input())

for val in values:  
    a, b = val.replace('\r', '').split(' ')

    try:
        print int(a) / int(b)
    except (ZeroDivisionError, ValueError, TypeError) as e:
        print "Error Code:", e

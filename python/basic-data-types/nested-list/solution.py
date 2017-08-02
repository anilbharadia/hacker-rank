# https://www.hackerrank.com/challenges/nested-list/problem

def get_second(students):
    small, second = 100, 100
    for s in students:
        score = s[1]
        if score < small:
            small, second = score, small
        elif score < second and score > small:
            second = score
    return second


students = [[raw_input(), float(raw_input())] for _ in range(int(raw_input())) ]
second = get_second(students)



names = [s[0] for s in students if s[1] == second]
names.sort()

for name in names:
    print name
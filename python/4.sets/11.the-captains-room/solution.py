raw_input()
all_rooms = raw_input().split()

for ur in set(all_rooms):
    count = 0
    found = True
    for r in all_rooms:
        if r == ur:
            count += 1
        if count > 1:
            found = False
            break
    if found:
        print ur
        break

# print [ t[0] for t in [(ur, all_rooms.count(ur)) for ur in set(all_rooms)] if t[1] == 1][0]

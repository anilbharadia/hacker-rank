raw_input()
all_rooms = raw_input().split()

for ur in set(all_rooms):
    if all_rooms.count(ur) == 1:
        print ur
        break

# print [ t[0] for t in [(ur, all_rooms.count(ur)) for ur in set(all_rooms)] if t[1] == 1][0]


list = []

for c in range(int(raw_input())):
    command = raw_input()

    args = command.split()

    if len(args) > 1:
        a = int(args[1])
    if len(args) > 2:
        b = int(args[2])
    if "insert" in command:
        list.insert(a, b)
    elif "print" == command:
        print list
    elif "remove" in command:
        list.remove(a)
    elif "append" in command:
        list.append(a)
    elif "sort" == command:
        list.sort()
    elif "pop" == command:
        list.pop()
    elif "reverse" == command:
        list.reverse()
import re

for r in range(int(raw_input())):
    try:
        re.compile(raw_input())
        print True
    except Exception:
        print False
students = [[raw_input(), float(raw_input())] for _ in xrange(int(raw_input()))]

unique_scores_sorted = sorted(set([s[1] for s in students]))

for name in sorted([s[0] for s in students if s[1] == unique_scores_sorted[1]]):
    print name
import sys

def luma(r, g, b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

data = sys.stdin.readlines()

flat_list = [val > 80 for sublist in [[luma(*[int(i) for i in pixel.split(',')]) for pixel in row.split()] for row in data] for val in sublist]

day_count = flat_list.count(True)
night_count = flat_list.count(False)

day_percent = day_count * 100 / (day_count + night_count)

if (day_percent > 50):
    print 'day'
else:
    print 'night'
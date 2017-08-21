import calendar

mm, dd, yyyy = [int(i) for i in raw_input().split()]

print calendar.day_name[calendar.weekday(yyyy, mm, dd)].upper()
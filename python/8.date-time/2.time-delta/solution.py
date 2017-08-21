import datetime

def get_tzs(z):
    hh = int(z[2:4])
    mm = int(z[4:6])
    ss = hh * 3600 + mm * 60
    return -ss if '+' in z else ss

date_format = '%a %d %b %Y %H:%M:%S'

for _ in xrange(int(raw_input())):
    # Sun 10 May 2015 13:54:36 -0700
    s1 = raw_input()
    z1 = s1[-6:]
    t1 = datetime.datetime.strptime(s1[:-6], date_format)
    
    s2 = raw_input()
    z2 = s2[-6:]
    t2 = datetime.datetime.strptime(s2[:-6], date_format)
    ans = (t1 - t2).total_seconds()
    
    ans += get_tzs(z1)
    ans -= get_tzs(z2)

    print int(abs(ans))


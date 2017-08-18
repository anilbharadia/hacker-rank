from collections import namedtuple

Point = namedtuple('Point', 'x,y')

p1 = Point(10, 15)

print p1

print p1.x

Car  = namedtuple('car', 'engine color Class speed')

mycar = Car(engine='java', Class='private', color='Red', speed='fast')
myoldcar = Car(engine='java', Class='private', color='Red', speed=16)
print mycar.speed
print myoldcar.speed*2
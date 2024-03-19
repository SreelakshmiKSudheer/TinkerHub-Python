from joy import *

p1 = point(x=0, y=100)
p2 = point(x=100, y=0)
p3 = point(x=0, y=-100)
p4 = point(x=-100, y=0)

shape = polygon([p1, p2, p3,p4])
show(shape)
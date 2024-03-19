from joy import *

# horizontal line
l = line()
show(l)

# inclined line
l1 = line(x1 = 0,y1 = 0, x2 = 100, y2 = 100)
show(l1)

# triangle
x1,y1 = 0,0
x2,y2 = 100,0
x3,y3 = 0,100

l1 = line(x1,y1,x2,y2)
l2 = line(x2,y2,x3,y3)
l3 = line(x3,y3,x1,y1)

show(l1)
show(l2)
show(l3)
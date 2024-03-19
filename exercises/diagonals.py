from joy import *

# here is the square
s = rectangle(w=200, h=200)
show(s)

# draw the diagonals
x1,y1 = -100,100
x2,y2 = -100,-100
x3,y3 = 100,100
x4,y4 = 100,-100

l1 = line(x1,y1,x4,y4)
l2 = line(x2,y2,x3,y3)
show(l1,l2)
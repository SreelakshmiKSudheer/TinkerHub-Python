from joy import *

# the top-right circle
c1 = circle(x=50, y=50, r=50)

# create the remaining three circles
c2 = circle(x=-50, y=50, r=50)
c3 = circle(x=-50, y=-50, r=50)
c4 = circle(x=50, y=-50, r=50)

# show the circles
show(c1,c2,c3,c4)
from joy import *

'''
# 3 circles in a row
c1 = circle(x=-100, y=0, r=50)
c2 = circle(x=0, y=0, r=50)
c3 = circle(x=100, y=0, r=50)
show(c1,c2,c3)
'''
# create the center circle
c1 = circle(x=0, y=0, r=50)

# create the top and the bottom
c2 = circle(x=0, y=100, r=50)
c3 = circle(x=0, y=-100, r=50)

# show the circles
show(c1,c2,c3)
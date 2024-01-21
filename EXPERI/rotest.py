from LIB.lne import *
from LIB.ThreeD import *
from math import *
p=pi/120
x1,y1=64,32
x2,y2=64,5
x3,y3=74,5
while 1:
  sp(0.2)
  clear_screen()
  x1,y1=t2rt(64,32,x1,y1,p)
  x2,y2=t2rt(64,32,x2,y2,p)
  x3,y3=t2rt(64,32,x3,y3,p)
  ln(int(x1),int(y1),int(x2),int(y2))
  ln(int(x2),int(y2),int(x3),int(y3))
  show_screen()
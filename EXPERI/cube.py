from LIB.lne import *
from LIB.ThreeD import *
p=pi/60
p2=pi/120
p3=pi/80
x,y,z=30,10,0
xa,ya,za=50,20,10
xc,yc,zc=x+xa/2,y+ya/2,z+za/2
#xc,yc,zc=21,21,51
x1,x2,x3,x4,x5,x6,x7,x8=x,x+xa,x,x+xa,x,x+xa,x,x+xa
y1,y2,y3,y4,y5,y6,y7,y8=y,y,y+ya,y+ya,y,y,y+ya,y+ya
z1,z2,z3,z4,z5,z6,z7,z8=z,z,z,z,z+za,z+za,z+za,z+za
try:
 while 1:
  x1,y1,z1=t3rt(xc,yc,zc,x1,y1,z1,p,p2,p3)
  x2,y2,z2=t3rt(xc,yc,zc,x2,y2,z2,p,p2,p3)
  x3,y3,z3=t3rt(xc,yc,zc,x3,y3,z3,p,p2,p3)
  x4,y4,z4=t3rt(xc,yc,zc,x4,y4,z4,p,p2,p3)
  x5,y5,z5=t3rt(xc,yc,zc,x5,y5,z5,p,p2,p3)
  x6,y6,z6=t3rt(xc,yc,zc,x6,y6,z6,p,p2,p3)
  x7,y7,z7=t3rt(xc,yc,zc,x7,y7,z7,p,p2,p3)
  x8,y8,z8=t3rt(xc,yc,zc,x8,y8,z8,p,p2,p3)
  clear_screen()
  ln3d(x1,y1,z1,x2,y2,z2)
  ln3d(x1,y1,z1,x3,y3,z3)
  ln3d(x2,y2,z2,x4,y4,z4)
  ln3d(x3,y3,z3,x4,y4,z4)
  
  ln3d(x1,y1,z1,x5,y5,z5)
  ln3d(x2,y2,z2,x6,y6,z6)
  ln3d(x3,y3,z3,x7,y7,z7)
  ln3d(x4,y4,z4,x8,y8,z8)
  
  ln3d(x5,y5,z5,x6,y6,z6)
  ln3d(x5,y5,z5,x7,y7,z7)
  ln3d(x6,y6,z6,x8,y8,z8)
  ln3d(x7,y7,z7,x8,y8,z8)
  
  show_screen()
except KeyboardInterrupt:
  pass
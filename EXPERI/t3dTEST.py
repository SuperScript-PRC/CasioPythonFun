from LIB.ThreeD import *
from LIB.lne import *
from casioplot import *
def cube(x,y,z,a):
  ln3d(x,y,z,x+a,y,z)
  ln3d(x,y,z,x,y+a,z)
  ln3d(x+a,y,z,x+a,y+a,z)
  ln3d(x,y+a,z,x+a,y+a,z)
  ln3d(x,y,z,x,y,z+a)
  ln3d(x+a,y,z,x+a,y,z+a)
  ln3d(x,y+a,z,x,y+a,z+a)
  ln3d(x+a,y+a,z,x+a,y+a,z+a)
  ln3d(x,y,z+a,x+a,y,z+a)
  ln3d(x,y,z+a,x,y+a,z+a)
  ln3d(x+a,y,z+a,x+a,y+a,z+a)
  ln3d(x,y+a,z+a,x+a,y+a,z+a)
x,y,z=1,1,1
xs,ys,zs=2,2,0
while 1:
  x+=xs
  y+=ys
  z+=zs
  zs+=1
  if x>=108 or x<=0:
    xs*=-1
    x=lim(1,127,x)
  if y>=50 or y<=0:
    ys*=-1
    y=lim(1,63,y)
  if z>=128:
    zs=-0.945*abs(zs)
  clear_screen()
  cube(x,y,z,20)
  ln3d(0,0,0,0,0,128)
  ln3d(128,0,0,128,0,128)
  ln3d(0,64,0,0,64,128)
  ln3d(128,64,0,128,64,128)
  ln3d(0,0,128,128,0,128)
  ln3d(0,0,128,0,64,128)
  ln3d(128,0,128,128,64,128)
  ln3d(0,64,128,128,64,128)
  show_screen()
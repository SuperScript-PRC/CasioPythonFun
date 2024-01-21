from casioplot import *
from math import *
t3dscal=0.01
def f3d(x,y,z):
  xdis=x-64 or 1
  ydis=y-32 or 1
  rx=64+xdis*1/(z*t3dscal+1 or 1)
  ry=32+ydis*1/(z*t3dscal+1 or 1)
  return int(rx),int(ry)
def dot3d(x,y,z):
  x,y=f3d(x,y,z)
  set_pixel(x,y)
def drt(x,y,a):
  if x==y==0:
    return x,y
  return x*cos(a)-y*sin(a),x*sin(a)+y*cos(a)
def t2rt(x0,y0,x,y,a):
  xd,yd=drt(x-x0,y-y0,a)
  return x0+xd,y0+yd
try:
  from lne import ln
except:
  from lib.lne import *
from math import sin,cos,sqrt,pi,asin
from casioplot import *
t3dscal=0.01
def f3d(x,y,z):
  xdis=x-64
  ydis=y-32
  rx=64+xdis*1/(z*t3dscal+1)
  ry=32+ydis*1/(z*t3dscal+1)
  return int(rx),int(ry)
def ln3d(x1,y1,z1,x2,y2,z2):
  (x1,y1),(x2,y2)=f3d(x1,y1,z1),f3d(x2,y2,z2)
  ln(x1,y1,x2,y2)
def dot3d(x,y,z):
  x,y=f3d(x,y,z)
  set_pixel(x,y)
def drt(x,y,a):
  if x==y==0:
    return x,y
  l=sqrt(x**2+y**2)
  sn=pi-asin(x/l) if y<0 else asin(x/l)
  sn-=a
  return l*sin(sn),l*cos(sn)
def t2rt(x0,y0,x,y,a):
  xd,yd=drt(x-x0,y-y0,a)
  return x0+xd,y0+yd
def t3rt(x0,y0,z0,x,y,z,a,b,c=0):
  x1,y1=t2rt(x0,y0,x,y,a)
  y1,z1=t2rt(y0,z0,y1,z,b)
  x1,z1=t2rt(x0,z0,x1,z1,c)
  return x1,y1,z1
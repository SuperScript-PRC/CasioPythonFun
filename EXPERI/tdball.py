from casioplot import *
from random import *
from LIB.ThreeD import *
from LIB.lne import *
balls=[]
tm=0
class ball:
  def __init__(s,x,y,z,xp=1,yp=0,zp=1):
    s.xsp=xp
    s.ysp=yp
    s.zsp=zp
    s.x=x
    s.y=y
    s.z=z
    s.a=0.5
  def nexts(s):
    x=s.x
    y=s.y
    z=s.z
    s.ysp+=s.a
    nextx=x+s.xsp
    nexty=y+s.ysp
    nextz=z+s.zsp
    if nextx<0:
      nextx=0
      s.xsp*=-1
    elif nextx>127:
      nextx=127
      s.xsp*=-1
    if nexty>=63:
      nexty=63
      s.ysp*=-1
    if nextz>=128:
      nextz=128
      s.zsp*=-1
    if nextz<=0:
      nextz=0
      s.zsp*=-1
    if z in range(124,128) and y in range(63,64):
      balls.remove(s)
    s.x=nextx
    s.y=nexty
    s.z=nextz
  def setdot(s):
    x,y=f3d(s.x,s.y,s.z)
    set_pixel(x,y)
    set_pixel(x-1,y)
    set_pixel(x,y-1)
    set_pixel(x-1,y-1)
rd=randint
while 1:
  ln3d(0,-64,128,0,64,128)
  ln3d(128,-64,128,128,64,128)
  ln3d(0,64,128,128,64,128)
  ln3d(0,64,0,0,64,128)
  ln3d(128,64,0,128,64,128)
  if len(balls)<1:
    balls+=[ball(choice((0,127)),rd(1,20),rd(1,20),rd(1,20))for i in range(1)]
  show_screen()
  sp(tm)
  clear_screen()
  for i in balls:
    i.nexts()
    i.setdot()
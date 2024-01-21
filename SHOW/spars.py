from casioplot import *
from math import *
from random import *
rr=0
class dot:
  def __init__(s):
    #global rr
    spd=randint(5,8)/8
    #rr+=14
    #ang=rr/360*2*pi
    ang=randint(1,360)*2*pi/360
    s.x,s.y=64,32
    s.xspd=spd*sin(ang)
    s.yspd=spd*cos(ang)
  def go(s):
    s.x+=s.xspd
    s.y+=s.yspd
  def draw(s):
    x=int(s.x)
    y=int(s.y)
    set_pixel(x-1,y-1)
    set_pixel(x-1,y)
    set_pixel(x,y-1)
    set_pixel(x,y)
    if x not in range(0,128) or y not in range(0,64):
      l.remove(s)
l=[]
tm=0
try:
 while 1:
  tm+=1
  clear_screen()
  if tm>5:
    tm=0
    l.append(dot())
  for i in l.copy():
    i.go()
    i.draw()
  show_screen()
except KeyboardInterrupt:
  pass
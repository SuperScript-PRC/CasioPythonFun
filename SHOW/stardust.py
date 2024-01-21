from random import *
from LIB.threed import *
from casioplot import *
class dot:
  def __init__(s):
    s.x=randint(-40,168)
    s.y=randint(-20,84)
    s.z=300
    s.spd=3
  def go(s):
    s.z-=s.spd
  def draw(s):
    x,y=f3d(s.x,s.y,s.z)
    set_pixel(x-1,y-1)
    if s.z<100:
      set_pixel(x-1,y)
      set_pixel(x,y-1)
      set_pixel(x,y)
    if s.z<=-80:
      if x in range(1,127) and y in range(1,64):
        l.append(tx(x,y))
      l.remove(s)
class tx:
  def __init__(s,x,y):
    s.t=80
    s.x,s.y=x,y
  def go(s):
    s.t-=1
  def draw(s):
    draw_string(s.x-2,s.y-3,"/")
    if s.t==0:
      l.remove(s)
l=[]
tmer=0
try:
 while 1:
  tmer+=1
  if tmer>8:
    tmer=0
    l.append(dot())
  clear_screen()
  for i in l.copy():
    i.go()
    i.draw()
  show_screen()
except KeyboardInterrupt:
  pass
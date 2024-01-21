from casioplot import *
from random import *
class snow:
  def __init__(s):
    s.x=randint(1,160)
    s.y=0
    s.spd=randint(3,6)/60+0.02
  def go(s):
    s.x-=s.spd
    s.y+=0.2
  def draw(s):
    x,y=int(s.x),int(s.y)
    set_pixel(x-1,y-1)
    set_pixel(x-1,y)
    set_pixel(x,y-1)
    set_pixel(x,y)
    if x<0 or y>64:
      l.remove(s)
l=[]
tm=0
textx=0
texty=0
try:
 while 1:
  tm+=1
  if tm>16:
    tm=0
    l.append(snow())
  clear_screen()
  for i in l.copy():
    i.go()
    i.draw()
  show_screen()
except KeyboardInterrupt:
 pass 
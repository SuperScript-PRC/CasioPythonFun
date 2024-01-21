#print("Low Power")
#raise SystemExit
from casioplot import *
from random import *
from LIB.lne import ln,sp
from LIB.ballib import *
from math import *
ballcnt=2
bcnt=1
balls=[]
tm=0.1
lv=1
def lns():
  global lv
  lv+=1  
  draw_string(20,1,"Level "+str(lv),zzz,"large")
  choice(
  (ln1,ln2,ln3,ln4,ln5,ln6,ln7,ln8,ln9)
  )()
tff=(255,255,255)
zzz=(0,0,0)
class ball:
  def __init__(s):
    ang=180/pi*randint(1,360)
    spd=randint(6,8)/4
    s.xsp=sin(ang)*spd
    s.ysp=cos(ang)*spd
    s.x=64;s.y=10;s.a=0.5
    s.ex=1
  def pdy(s,x,y):
    x,y=int(x),int(y)
    if get_pixel(x,y+1)==(0,0,0):
      s.ysp=-0.9*abs(s.ysp)
      return 1
    elif get_pixel(x,y-2)==(0,0,0):
      s.ysp=abs(s.ysp)
      return 1
  def pdx(s,x,y):
    x,y=int(x),int(y)
    if get_pixel(x-2,y+1)==zzz or get_pixel(x-2,y)==zzz:
      s.xsp=abs(s.xsp)
      set_pixel(x-2,y+1,tff)
      set_pixel(x-2,y,tff)
      return 1
    elif get_pixel(x+1,y+1)==zzz or get_pixel(x+1,y)==zzz:
      s.xsp=-abs(s.xsp)
      set_pixel(x+1,y,tff)
      set_pixel(x+1,y+1,tff)
      return 1
  def nexts(s):
    x=int(s.x)
    y=int(s.y)
    s.ysp+=s.a
    nextx=x+s.xsp
    nexty=y+s.ysp
    if nextx<0:
      nextx=0
      s.xsp*=-1
    elif nextx>127:
      nextx=127
      s.xsp*=-1
    if nexty>=63:
      s.ex=0
      draw_string(s.x,10,"ok")
      balls.remove(s)
    if s.ysp>0:
      for i in range(y+1,nexty+1):
        if s.pdy(x,i):
          break
        s.y=i
    elif s.ysp<0:
      for i in range(y-1,nexty-1,-1):
        if s.pdy(x,i):
          break
        s.y=i
    if s.xsp>0:
      for i in range(x+1,nextx+1):
        if s.pdx(i,s.y):
          break
        s.x=i
    elif s.xsp<0:
      for i in range(x-1,nextx-1,-1):
        if s.pdx(i,s.y):
          break
        s.x=i
  def setdot(s):
    if not s.ex:return
    set_pixel(int(s.x)-1,int(s.y)-1)
    set_pixel(int(s.x)-1,int(s.y))
    set_pixel(int(s.x),int(s.y)-1)
    set_pixel(int(s.x),int(s.y))
  def clr(s):
    n=(255,255,255)
    set_pixel(int(s.x)-1,int(s.y)-1,n)
    set_pixel(int(s.x)-1,int(s.y),n)
    set_pixel(int(s.x),int(s.y)-1,n)
    set_pixel(int(s.x),int(s.y),n)
bck=globals()
while 1:
 try:
  if "ball" not in globals():
    globals().update(bck)
    ln(0,1,128,1)
  if len(balls)<bcnt:
    balls+=[
    ball()for i in range(ballcnt)
    ]
    clear_screen()
    lns()
  show_screen()
  sp(tm)
  for i in balls:
    i.clr()
  for i in balls.copy():
    i.nexts()
    i.setdot()
 except KeyboardInterrupt:
   try:
     b=balls[0]
     print("xspd:",b.xsp,"\nyspd:",b.ysp)
     print("x:",b.x,"y:",b.y)
     print("xp:",b.pdx(b.x,b.y))
     try:
       s=input()
       tm=float(s or "0")
     except ValueError:
       balls=[]
       tm=0.1
     #raise Exception("last long",s)
     draw_string(0,0,str(tm))
   except KeyboardInterrupt:
     break
from LIB.ThreeD import *
from LIB.lne import sp
from LIB.gzp import *
from LIB.chars import *
from random import randint as rd
from casioplot import *
sce=[]
class dot:
  def __init__(s,x,y):
    s.x,s.y=x,y
    s.spd=rd(5,20)/20
    s.z=0
  def go(s):
    s.x+=s.spd
    if s.x>128:
      sce.remove(s)
  def go2(s):
    s.x,s.y=t2rt(64,32,s.x,s.y,0.05)
    s.z-=2
    if s.z<-90:
      sce.remove(s)
  def show(s):
    x,y=f3d(s.x,s.y,s.z)
    bigdot(x,y)
def main():
  sce.clear()
  timer=0
  flash=1
  for i in range(20):
    sce.append(dot(rd(1,128),rd(1,64)))
  try:
   while 1:
    clear_screen()
    if timer==0:
      sce.append(dot(0,rd(1,64)))
      timer=10
      flash*=-1
    timer-=1
    if flash==1:
      draw_string(45,35,"PUSH START")
    for i in sce.copy():
      i.go()
      i.show()
    draw_string(24,19,"The Story of Stelle")
    draw_string(12,25,"Honkai: Star Rail",(0,0,0),"large")
    draw_string(33,52,"1994 MiHoYo Ltd.")
    draw_string(25,58,"All rights reserved.")
    show_screen()
    sp(0.1)
  except:pass
  cdy,cdys,cdya=25,0,0.1
  try:
   while sce or cdy<5:
    cdy+=cdys
    cdys+=cdya
    clear_screen()
    draw_string(12,int(cdy),"Honkai: Star Rail",(0,0,0),"large")
    draw_string(24,int(cdy-6),"The Story of Stelle")
    for i in sce.copy():
      i.go2()
      i.show()
    show_screen()
   clear_screen()
   drawchr(35,25,chrs["xing1"])
   drawchr(45,25,chrs["tie3"])
   drawchr(55,25,chrs["qi3"])
   drawchr(65,25,chrs["dong4"])
   drawchr(75,25,chrs["!"])
   while 1:
    for cl in ((0,0,0),(255,255,255)):
     sp(0.2)
     drawchr(15,36,chrs["yin2"],cl)
     drawchr(25,36,chrs["lang2"],cl)
     drawchr(35,36,chrs["he2"],cl)
     drawchr(45,36,chrs["san1"],cl)
     drawchr(55,36,chrs["yue4"],cl)
     drawchr(65,36,chrs["qi1"],cl)
     drawchr(75,36,chrs["xi3"],cl)
     drawchr(85,36,chrs["huan1"],cl)
     drawchr(95,36,chrs["wo3"],cl)
  except:pass
main()
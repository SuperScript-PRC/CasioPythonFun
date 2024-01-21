from casioplot import *
from random import *
from math import *
lst=[]
rsp=200
yspd=1
hackpgs=0
class snt:
  def __init__(s):
    s.t=rndprg()
    s.y=len(lst)*10
  def show(s):
    s.y-=yspd
    tt=s.y%12
    if tt<6:
      x=tt
    else:
      x=12-tt
    draw_string(int(x),int(s.y),s.t,(0,0,0),"large")
    if s.y<-10:
      lst.remove(s)
mhex=lambda w:("%.2x"%randint(0,16**w)).upper()
cabc=lambda :choice("abcdef").upper()
def hckshow(h):
  global rsp
  mx=400
  draw_string(47,47,"SilverWolf")
  if h<mx:
    p=int(h/mx*20)
    p1=int(h/mx*100)
    draw_string(
    1,54,"["+"="*p+"-"*(20-p)+"] "+str(p1)+"%")
  else:
    global yspd
    if yspd>0.2:
      yspd-=0.01
    if h%(mx/10)<mx/20:
      draw_string(28,26,"[ Hack OK! ]",(0,0,0),"large")
    draw_string(1,54,"["+"="*20+"] 100%",)
def rndprg():
  r=randint(1,10)
  if r==1:return"ADD %s, %d"%(choice("ABCDEF"),randint(1,255))
  elif r==2:return"ADD %s, %s"%(choice("ABCDEF"),choice("ABCDEF"))
  elif r==3:return"MOV ebp, eax+%d"%randint(0,8)
  elif r==4:return"IN "+mhex(4)+", "+cabc()
  elif r==5:return"OUT "+cabc()+", "+mhex(4)
  elif r==6 or r==7:return"CMP "+cabc()+", "+cabc()
  elif r==8:return"CALL "+mhex(4)
  elif r==9:return"JMP "+mhex(4)
  elif r==10:return"LDA "+mhex(4)+", "+cabc()
while 1:
 try:
  hackpgs+=1
  clear_screen()
  hckshow(hackpgs)
  while len(lst)<8:
    lst.append(snt())
  for i in lst.copy():
    i.show()
  for i in range(rsp):
    show_screen()
 except KeyboardInterrupt:
  if hackpgs<400:
    hackpgs+=20 
  else:
    break
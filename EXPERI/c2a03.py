from LIB.lne import *
from random import randint as rd
rng=range(0,128)
def mksq(tone,x,v=5):
  if tone==0:return 0
  t=480/tone
  if x%t<t/2:return v
  else:return 0
def mktri(tone,x,v=10):
  if tone==0:return 0
  t=960/tone
  xd=x%t
  if xd<t/2:return v*(xd/t)*2
  else:return v*2-v*(xd/t)*2
def wav(l):
  t1,t2,t3=l
  clear_screen()
  y=32
  for x in rng:
    s=48
    s-=mksq(t1,x-64)+mksq(t2,x-64)+mktri(t3,x-64)
    ln(x-2,y,x-1,int(s))
    y=int(s)
  show_screen()
while 1:
  wav([rd(10,60),rd(10,60),rd(10,30)])
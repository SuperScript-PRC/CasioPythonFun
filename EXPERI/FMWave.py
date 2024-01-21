from LIB.lne import *
from math import *
long=range(25,105)
fmlist=[
(15,0.2,0,0,0,20),
(5,0.3,5,0,0.2,50),
]
def opto(awps,t,x):
  a,w,p,a1,w1,p1=awps
  return (a-a1*t/100)*sin(
    (w-w1*t/100)*x+
    (p-p1*t/100))
def mkwav(lst):
  for t in range(0,101):
    clear_screen()
    lasty=0
    for x in long:
      w=32
      for l in lst:
        w-=opto(l,t,x-64)
      if lasty:
        ln(x-1,int(lasty),x,int(w))
      lasty=w
    show_screen()
mkwav(fmlist)
cl="0123456789abcdefghijklmnopqrstuvwxyz"
from casioplot import *
def drawchr(x,y,chart,cl=(0,0,0)):
  y1=-1
  for i in chart.split():
    x1=-1
    y1+=1
    for j in ecn(i):
      x1+=1
      if j=="1":
        set_pixel(x+x1,y+y1,cl)
def ecn(t):
  s=0
  for i in range(0,len(t)):
    s+=cl.find(t[i])*len(cl)**(len(t)-1-i)
  res=bit(s)
  return "0"*(9-len(res))+res
def ect(n,mins=1):
  s=""
  while n>0:
    n,b=divmod(n,len(cl))
    s=cl[b]+s
  return "0"*(mins-len(s))+s if len(s)<mins else s
def bit(n):
  r=""
  while n>0:
    n,b=divmod(n,2)
    r=str(b)+r
  return r
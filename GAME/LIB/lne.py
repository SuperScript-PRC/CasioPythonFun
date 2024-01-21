from casioplot import *
p2n=lambda n:1 if n>=0 else -1
def ln(x1,y1,x2,y2,c=(0,0,0)):
 if y2-y1==x2-x1==0:return
 k=(y2-y1)/(x2-x1) if x2-x1 else 2
 b=y1-k*x1
 if abs(k)<=1:
   st=p2n(x2-x1)
   for i in range(x1,x2+st,st):
     set_pixel(i,int(k*i+b),c)
 else:
   k=(x2-x1)/(y2-y1)
   b=x1-k*y1
   st=p2n(y2-y1)
   for i in range(y1,y2+st,st):
     set_pixel(int(k*i+b),i,c)
def sp(t):
  for i in range(int(5000*t)):
    show_screen()
def lntxt(x,y,l):
  lns=l.split("\n")
  for i in range(len(lns)):
    draw_string(x,y+8*i,lns[i],(0,0,0),"large")
  show_screen()
def grey(x,y):
  b=1
  for i in range(x*8-2,x*8+7):
    for j in range(y*8-2,y*8+7):
      b*=-1
      if b==1:set_pixel(i,j)
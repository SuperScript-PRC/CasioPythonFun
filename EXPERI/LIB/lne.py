from casioplot import *
p2n=lambda n:1 if n>=0 else -1
def lim(x,y,m):
  return min(max(m,x),y)
def ln(x1,y1,x2,y2):
 if y2-y1==x2-x1==0:return
 k=(y2-y1)/(x2-x1) if x2-x1 else 2
 b=y1-k*x1
 if abs(k)<=1:
   st=p2n(x2-x1)
   for i in range(x1,x2+st,st):
     set_pixel(i,int(k*i+b))
     #sp(0.01)
 else:
   k=(x2-x1)/(y2-y1)
   b=x1-k*y1
   st=p2n(y2-y1)
   for i in range(y1,y2+st,st):
     set_pixel(int(k*i+b),i)
     #sp(0.01)
def bigdot(x,y):
  set_pixel(x-1,y-1)
  set_pixel(x,y-1)
  set_pixel(x-1,y)
  set_pixel(x,y)
def rect(x,y,x1,y1):
  ln(x,y,x1,y)
  ln(x,y,x,y1)
  ln(x1,y,x1,y1+1)
  ln(x,y1,x1,y1)
def sp(t):
  for i in range(int(5000*t)):
    show_screen()
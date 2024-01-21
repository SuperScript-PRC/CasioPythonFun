from casioplot import *
p2n=lambda n:1 if n>=0 else -1
def lim(x,y,m):
  return min(max(m,x),y)
def ln(x1,y1,x2,y2):
 if y2-y1==x2-x1==0:return
 k=(y2-y1)/(x2-x1) if x2-x1 else 2
 b=y1-k*x1
 if abs(k)<=1:
   for i in range(x1,x2,p2n(x2-x1)):
     set_pixel(i,int(k*i+b))
     #sp(0.04)
 else:
   k=(x2-x1)/(y2-y1)
   b=x1-k*y1
   for i in range(y1,y2,p2n(y2-y1)):
     set_pixel(int(k*i+b),i)
     #sp(0.04)
def sp(t):
  for i in range(int(5000*t)):
    show_screen()
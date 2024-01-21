from casioplot import *
def ani():
 try:
  clear_screen()
  show_screen()
  ln(0,15,120,30)
  ln(0,20,120,30)
  ln(0,25,120,30)
  draw_string(116,26,"Q")  
  sp(0.5)
  clear_screen()
  ln(0,12,110,22)
  ln(0,18,110,22)
  ln(0,24,110,22)  
  draw_string(106,18,"Q")
  sp(0.5)
  clear_screen()
  ln(0,12,110,25)
  ln(0,18,110,25)
  ln(0,24,110,25)
  draw_string(106,21,"Q")
  sp(0.5)
  clear_screen()
  ln(0,12,120,30)
  ln(0,18,120,30)
  ln(0,24,120,30)
  draw_string(116,26,"Q")
  sp(0.5)
  clear_screen()
  ln(0,12,120,35)
  ln(0,18,120,35)
  ln(0,24,120,35)
  draw_string(116,31,"Q")
  sp(0.5)
  clear_screen()
  ln(0,8,110,40)
  ln(0,14,110,40)
  ln(0,22,110,40)
  draw_string(106,36,"Q")
  sp(0.5)
  clear_screen()
  ln(0,8,110,45)
  ln(0,14,110,45)
  ln(0,22,110,45)
  draw_string(106,41,"Q")
  sp(0.5)
  clear_screen()
  ln(0,4,100,45)
  ln(0,12,100,45)
  ln(0,20,100,45)
  draw_string(96,41,"Q")
  sp(0.5)
  clear_screen()
  ln(4,5,90,43)
  ln(0,20,90,43)
  ln(4,35,90,43)
  draw_string(86,39,"Q")
  sp(0.5)
  clear_screen()
  ln(4,-5,70,43)
  ln(0,10,70,43)
  ln(4,20,70,43)
  draw_string(66,39,"Q")
  sp(0.5)
  clear_screen()
  ln(20,-10,70,43)
  ln(12,0,70,43)
  ln(4,10,70,43)
  draw_string(66,39,"Q")
  sp(0.5)
  clear_screen()
  ln(50,0,70,43)
  ln(60,0,70,43)
  ln(75,0,70,43)
  draw_string(66,39,"Q")
  sp(0.5)
  clear_screen()
  ln(50,0,70,53)
  ln(60,0,70,53)
  ln(75,0,70,53)
  draw_string(66,49,"Q")
  sp(0.5)
  clear_screen()
  ln(47,0,70,50)
  ln(60,0,70,50)
  ln(78,0,70,50)
  draw_string(66,46,"Q")
  sp(0.5)
  clear_screen()
  ln(30,0,70,45)
  ln(55,0,70,45)
  ln(85,0,70,45)
  draw_string(65,40,"o",(255,255,255),"large")
  sp(0.5)
  clear_screen()
  ln(10,0,70,45)
  ln(55,0,70,45)
  ln(100,0,70,45)
  draw_string(65,40,"O",(255,255,255),"large")
  sp(0.5)
  clear_screen()
  ln(0,10,50,45)
  ln(64,0,70,45)
  ln(70,45,128,10)
 except KeyboardInterrupt:
   ...
def sp(t):
  for i in range(int(5000*t)):
    show_screen()   
p2n=lambda n:1 if n>=0 else -1
def ln(x1,y1,x2,y2):
 if y2-y1==x2-x1==0:return
 k=(y2-y1)/(x2-x1) if x2-x1 else 2
 b=y1-k*x1
 if abs(k)<=1:
   for i in range(x1,x2,p2n(x2-x1)):
     set_pixel(i,int(k*i+b))
 else:
   k=(x2-x1)/(y2-y1)
   b=x1-k*y1
   for i in range(y1,y2,p2n(y2-y1)):
     set_pixel(int(k*i+b),i)
 show_screen()
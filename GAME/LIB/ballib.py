from LIB.lne import sp,ln
from random import *
from math import *
rd=randint
from casioplot import *
def ln1():
  for j in range(30,65):
    for i in range(1,129):
      if choice((0,1,1)):
        set_pixel(i,j)
    show_screen()
def ln2():
  for i in range(25):
    y1,y2=rd(20,80),rd(20,80)
    if abs(y1-y2)<3:y1-=5
    ln(0,y1,128,y2)
    show_screen()
def ln3():
  for i in range(0,128,3):
    for j in range(25,64,5):
      draw_string(i,j,chr(rd(20,126)))
      sp(0.01)
    show_screen()
def ln4():
  for i in range(80):
    x,y=rd(-20,120),rd(20,60)
    a=rd(5,20)
    ln(x,y,x+a,y)
    ln(x,y,x,y+a)
    ln(x+a,y,x+a,y+a)
    ln(x,y+a,x+a,y+a)
    show_screen()
def ln5():
  for x in range(0,128,5):
    for y in range(20,64,7):
      draw_string(x,y,chr(rd(65,90)),(0,0,0),"large")
      sp(0.01)
def ln6():
  for y in range(20,64,6):
    x1,x2=rd(1,125),rd(3,8)
    ln(0,y,x1,y)
    ln(x1+2,y,128,y)
    for i in range(128):
      if random()>0.9:
        ln(i,y-5,i,y)
    show_screen()
def ln7():
  for i in range(20,64,8):
    ln(5,i,128,i)
    ln(0,i+4,123,i+4)
    show_screen()
def ln8():
  for i in range(30,63):
    sr=rd(1,126)
    ln(0,i,sr,i)
    ln(sr+2,i,128,i)
  for i in range(50):
    r,s=rd(20,108),rd(30,55)
    ln(
    r,s,
    r+rd(-5,5),s+rd(-5,5),
    (255,255,255))
  r=randint(10,100)
  ln(r,50,r+rd(-5,5),64,(255,255,255))
def ln9():
  for ix in range(10,135,15):
   for iy in range(30,70,10):
    r=randint(6,15)
    x=randint(-5,5)+ix
    y=randint(-5,5)+iy
    for a in range(144):
      set_pixel(round(r*sin(a/72*pi)+x),round(r*cos(a/72*pi)+y))
    show_screen()
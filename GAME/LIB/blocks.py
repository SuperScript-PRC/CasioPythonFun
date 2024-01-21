from LIB.lne import *
def white(x,y):
  for i in range(x,x+8):
    for j in range(y,y+8):
      set_pixel(i,j,(255,255,255))
def b1(x,y,c=(0,0,0)):
  ln(x,y,x+6,y,c)
  ln(x,y,x,y+6,c)
  ln(x+6,y,x+6,y+6,c)
  ln(x,y+6,x+6,y+6,c)
def b2(x,y,c=(0,0,0)):
  r=1
  for i in range(x,x+7):
    for j in range(y,y+7):
      r*=-1
      if r==1:set_pixel(i,j,c)
def b3(x,y,c=(0,0,0)):
  ln(x,y+3,x+3,y,c)
  ln(x,y+3,x+3,y+6,c)
  ln(x+3,y,x+6,y+3,c)
  ln(x+3,y+6,x+6,y+3,c)
def b4(x,y,c=(0,0,0)):
  ln(x+2,y,x,y+2,c)
  set_pixel(x+3,y+1,c)
  ln(x+4,y,x+6,y+2,c)
  ln(x,y+3,x+3,y+6,c)
  ln(x+3,y+6,x+6,y+3,c)
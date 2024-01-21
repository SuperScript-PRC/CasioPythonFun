m1=[1]*9;m2=[2]*9
m3=[3]*9;m4=[4]*9
m5=[5]*9;m6=[6]*9
from LIB.lne import ln;from casioplot import *
def show(m):
  for x in range(10,59,16):
    ln(x,10,x,59)
  for y in range(10,59,16):  
    ln(10,y,59,y)
  for i in range(9):
    py,px=divmod(i,3)
    draw_string(
    15+16*px,15+16*py,str(m[i]),(0,0,0),"large")
  dbg(70,5,m1)
  dbg(100,5,m2)
  dbg(70,25,m3)
  dbg(100,25,m4)
  dbg(70,45,m5)
  dbg(100,45,m6)
  show_screen()
def dbg(x,y,m):
  m=list(str(i) for i in m)
  draw_string(x,y," ".join(m[0:3]))
  draw_string(x,y+6," ".join(m[3:6]))
  draw_string(x,y+12," ".join(m[6:9]))
  show_screen()
def niu(op):
  global m1,m2,m3,m4,m5,m6
  if op==1:
    m4[0],m4[1],m4[2],m6[0],m6[1],m6[2],m2[0],m2[1],m2[2],m1[0],m1[1],m1[2],m3[2],m3[5],m3[8],m3[7],m3[6],m3[3],m3[0],m3[1]=\
    m1[0],m1[1],m1[2],m4[0],m4[1],m4[2],m6[0],m6[1],m6[2],m2[0],m2[1],m2[2],m3[8],m3[7],m3[6],m3[3],m3[0],m3[1],m3[2],m3[5]
  elif op==2:
    m4[3],m4[4],m4[5],m6[3],m6[4],m6[5],m2[3],m2[4],m2[5],m1[3],m1[4],m1[5]=\
    m1[3],m1[4],m1[5],m4[3],m4[4],m4[5],m6[3],m6[4],m6[5],m2[3],m2[4],m2[5]
  elif op==3:
    m4[6],m4[7],m4[8],m6[6],m6[7],m6[8],m2[6],m2[7],m2[8],m1[6],m1[7],m1[8],m3[8],m3[7],m3[6],m3[3],m3[0],m3[1],m3[2],m3[5]=\
    m1[6],m1[7],m1[8],m4[6],m4[7],m4[8],m6[6],m6[7],m6[8],m2[6],m2[7],m2[8],m3[2],m3[5],m3[8],m3[7],m3[6],m3[3],m3[0],m3[1]
  elif op==4:
    m5[0],m5[3],m5[6],m6[0],m6[3],m6[6],m3[0],m3[3],m3[6],m1[0],m1[3],m1[6],m2[8],m2[7],m2[6],m2[3],m2[0],m2[1],m2[2],m2[5]=\
    m1[0],m1[3],m1[6],m5[0],m5[3],m5[6],m6[0],m6[3],m6[6],m3[0],m3[3],m3[6],m2[2],m2[5],m2[8],m2[7],m2[6],m2[3],m2[0],m2[1]
  elif op==5:
    m5[1],m5[4],m5[7],m6[1],m6[4],m6[7],m3[1],m3[4],m3[7],m1[1],m1[4],m1[7]=\
    m1[1],m1[4],m1[7],m5[1],m5[4],m5[7],m6[1],m6[4],m6[7],m3[1],m3[4],m3[7]
  elif op==6:      
    m5[2],m5[5],m5[8],m6[2],m6[5],m6[8],m3[2],m3[5],m3[8],m1[2],m1[5],m1[8],m4[8],m4[7],m4[6],m4[3],m4[0],m4[1],m4[2],m4[5]=\
    m1[2],m1[5],m1[8],m5[2],m5[5],m5[8],m6[2],m6[5],m6[8],m3[2],m3[5],m3[8],m4[6],m4[3],m4[0],m4[1],m4[2],m4[5],m4[8],m4[7]
def nextm(op):
  global m1,m2,m3,m4,m5,m6
  if op==1:m2,m6,m4,m1=m1,m2,m6,m4
  elif op==2:m3,m6,m5,m1=m1,m3,m6,m5
  elif op==3:m4,m6,m2,m1=m1,m4,m6,m2
  elif op==4:m5,m6,m3,m1=m1,m5,m6,m3
while 1:
  try:
    clear_screen()
    show(m1)
    print(">>>")
    while 1:
      show_screen()
  except KeyboardInterrupt:
    while 1:
      try:
        op=[int(i) for i in input()]
        if op==[]:
          op=[1,0]
        nextm(op[0])
        niu(op[1])
        break
      except Exception as err:
        print(err)
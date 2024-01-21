from casioplot import *
from LIB.blocks import *
from random import *
p2n=lambda x:1 if x>=0 else -1
class block:
  def __init__(s,x,y,sz=None):
    fcs=(b1,b2,b3,b4)
    if sz:
      s.type=sz
      s.sz=fcs[sz]
    else:
      s.type=randint(0,len(fcs)-1)
      s.sz=fcs[s.type]
    s.x,s.y=x*8,y*8
  def show(s):
    s.sz(s.x,s.y)
  def move(s,nx,ny):
    sx,sy=s.x,s.y
    xd,yd=p2n(nx*8-s.x),p2n(ny*8-s.y)
    setp(s.x/8,s.y/8,None)
    for x0 in range(sx,nx*8+xd,xd):
      for y0 in range(sy,ny*8+yd,yd):
        s.x=x0
        s.y=y0
        s.sz(x0,y0-1,(255,255,255))
        s.sz(x0,y0)
        #sp(0.1)
        show_screen()
    setp(s.x/8,s.y/8,s)
  def delete(s):
    setp(s.x/8,s.y/8,None)
    white(s.x,s.y)
    show_screen()
def flush():
  clear_screen()
  axis()
  for i in bs:
    for j in i:
      if j:
        j.show()
  show_screen()
def chkxiao(x,y):
  j=getp(x,y)
  if j:
    for k,l in ((x-1,y-1),(x+1,y),(x,y-1),(x,y+1)):
      r=getp(k,l)
      if r and r.type==j.type:
        sp(0.2)
        xiao(x,y,0)
        break
def xiao(x,y,depth=0):
  b=getp(x,y)
  if b:
    b.delete()
    for i,j in ((x-1,y),(x,y-1),(x+1,y),(x,y+1)):
      b1=getp(i,j)
      if b1 and b1.type==b.type:
        sp(0.2)
        try:
          xiao(i,j)
        except RuntimeError:
          break
  if depth==0:
    flushb()
def flushb():
 ok=False
 while not ok:
  ok=True
  for j in bs:
   for i in j.copy():
    if i:
     while 1:
      r=getp(int(i.x/8),int(i.y/8+1))
      if r==None and i.y<50:
        i.move(int(i.x/8),int(i.y/8+1))
        ok=False
      else:
        break
     chkxiao(i.x/8,i.y/8)
  flush()
inrange=lambda x,y:x in range(1,16)and y in range(1,8)
getp=lambda x,y:bs[int(y-1)][int(x-1)] if inrange(x,y) else None
def setp(x,y,s):
  if inrange(x,y):
    bs[int(y-1)][int(x-1)]=s
def init():
  global bs
  bs=[[None for j in range(1,16)]for i in range(1,8)]
  for i in range(1,16):
    for j in range(1,8):
      setp(i,j,block(i,j))
def axis():
  for i in range(1,16):
    draw_string(i*8,1,str(i))
  for i in range(1,8):
    draw_string(1,i*8,str(i))
  ln(0,6,128,6)
  ln(6,0,6,64)
  show_screen()
log10=xiao
init()
flush()
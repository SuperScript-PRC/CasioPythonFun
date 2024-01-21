from casioplot import *
from random import *
from LIB.lne import ln,grey,sp
def tan():
  global mp
  clear_screen()
  l.clear();bbs.clear();lgs.clear()
  axis()
  mp=[""for i in range(105)]
  log10(1,1)
while 1:
  try:
    lb=int(input("bombs(1~40):"))
    assert lb in range(1,41)
    break
  except (AssertionError,ValueError):
    print("error")
class bomb:
  def __init__(s,x,y):
    s.x,s.y=x,y
  def draw(s):
    draws(s.x,s.y,"X")
inrange=lambda x,y:x in range(1,16) and y in range(1,8)
isempty=lambda x,y:mp[x-1+(y-1)*15]in ("","P")
def log(x,y,show=True):
  assert inrange(x,y),"out of range"
  if (x,y) in lgs:
    lgs.remove((x,y))
    draws(x,y,"")
    if show:flush()
  elif not isempty(x,y):
    print("not empty")
  else:
    lgs.append((x,y))
    draws(x,y,"P")
    if show:flush()
def draws(x,y,s):
  mp[(y-1)*15+x-1]=s
def chkwin():
  win=True
  for x in range(1,16):
    for y in range(1,8):
      if (x,y) not in bbs and isempty(x,y):
        win=False
  return win  
def gtlei(x,y,l):
  s=0
  for i in l:
    if i.x==x and i.y==y:
      return -1
    dx,dy=i.x-x,i.y-y
    if abs(dx)<2 and abs(dy)<2:
      s+=1
  return s
def canrm(x,y):
  if mp[x-1+(y-1)*15]:return False
  for i,j in ((x-1,y),(x+1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)):
    if not inrange(i,j):continue
    if mp[i-1+(j-1)*15]=="0":log10(x,y,1);return True
  return False
def rm0(x,y,depth):
  if depth>0:
    return
  rr=True
  while rr:
   rr=False
   for x0 in range(1,16):
    for y0 in range(1,8):
      if canrm(x0,y0):rr=False
def axis():
  for i in range(1,16):
    draw_string(i*8,1,str(i))
  for i in range(1,8):
    draw_string(1,i*8,str(i))
  ln(0,6,128,6)
  ln(6,0,6,64)
  show_screen()
def first(x,y,mn=20):
  while len(l)<mn:
    x0,y0=randint(1,15),randint(1,7)
    if x0 not in range(x-1,x+2) or y0 not in range(y-1,y+2):
      for i in l:
        if i.x==x0 and i.y==y0:
          break
      else:
        l.append(bomb(x0,y0))
        bbs.append((x0,y0))
  for x0 in range(x-1,x+2):
    for y0 in range(y-1,y+2):
      if inrange(x0,y0):
        log10(x0,y0,0)
def bgtext(x,y,t):
  for x0 in range(x,x+7*len(t)):
    for y0 in range(y,y+9):
      set_pixel(x0,y0,(0,0,0))
  draw_string(x+1,y+1,t,(255,255,255),"large")
  show_screen()    
def log10(x,y,depth=0):
  assert inrange(x,y),"out of range"
  if not l:
    first(x,y,lb)
  r=gtlei(x,y,l)
  if r>-1:
    draw_string(x*8,y*8,str(r))
    draws(x,y,str(r))
  if depth==0:flush()
  sp(0.01)
  rm0(x,y,depth)
  if r==-1:
    dead()
  elif depth==0 and chkwin():
    bgtext(25,28,"You win!!")
def flush():
  clear_screen()
  axis()
  for x in range(1,16):
    for y in range(1,8):
      r=mp[(x-1)+(y-1)*15]
      if r=="P":
        grey(x,y)
      elif r:
        draw_string(x*8,y*8,r)
  draw_string(1,1,str(ups))
  show_screen()
def dead():
  global ups
  try:
    if ups:
      for i in range(5,0,-1):
        bgtext(20,28,"Continue? %d"%i)
        sp(2.5)
    for i in l:
      i.draw()
      flush()
      sp(0.3)
    bgtext(25,28,"Game Over")
  except KeyboardInterrupt:
    if ups:
      ups-=1
    flush()
ups=3
l,bbs,lgs=[],[],[]
mp=[""for i in range(105)]
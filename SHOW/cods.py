from casioplot import *
from random import *
def rchr(gg):
  r=randint(65,112+gg)
  return (r if r<90 else r+7) if r<112 else 32
def mark(mp,gg):
  y=randint(0,5)
  x=randint(0,17)
  mp[y][x]=chr(rchr(gg))
def draw(mp):
  for y in range(6):
    for x in range(18):
      draw_string(
      x*7+1+randint(-1,0),
      y*10+1+randint(-1,0),
      mp[y][x],(0,0,0),"large")
mp=[[""]*21 for i in range(6)]
nset=0
try:
 while 1:
  nset+=1
  clear_screen()
  if nset%300<150:
    for i in range(5):
      mark(mp,10)
  else:
    for i in range(5):
      mark(mp,300)
  draw(mp)
  show_screen()
except KeyboardInterrupt:
  pass
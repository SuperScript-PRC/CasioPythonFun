from LIB.lda import loading
loading("Loading mst..")
from LIB.monster import mob
loading("Loading obj..")
from LIB.usedj import *
loading("Loading map..")
from LIB.mapelem import *
from random import random as rd, choice
def spawn(x,y):
  r=int(rd()*1000)
  if r in range(0,6):
    return money(x,y)
  elif r in range(6,12):
    return mob(x,y)
  elif r in range(12,17):
    return box(x,y)
  elif r in range(17,19):
    return trader(x,y)
  elif r in range(19,23):
    return bush(x,y)
  elif r in range(23,26):
    return barr(x,y)
  else:
    return None
def drawmap(its,x,y):
  mp=[[" "]*21 for i in range(6)]
  for it in its:
    if it.y-y in range(0,6)and it.x-x in range(0,21):
      mp[it.y-y][it.x-x]=it.t
  mp[3][10]="M";m=""
  for y0 in mp:
    for x0 in y0:
      m+=x0
    m+="\n"
  print(m[:-1])
def dealmvmp(mp,bd,x,y):
  rsp=[]
  for i in mp.copy():
    if isinstance(i,(mob,tnt,schar)):
      r=i.mvact(mp,bd,x,y)  
      if r:rsp+=r.split("\n")
  return rsp
def move(x,y,mp,bd,x1,y1):
  res=[]
  x+=x1
  y+=y1
  for it in mp.copy():
    if (it.x-x not in range(-3,25) or 
    it.y-y not in range(-3,10)):
      mp.remove(it)
  capp=lambda a:(mp.append(a) if a else None)
  if x1>0:
    for i in range(6):
      capp(spawn(x+20,y+i))
  if x1<0:
    for i in range(6):
      capp(spawn(x,y+i))
  if y1>0:
    for i in range(21):
      capp(spawn(x+i,y+5))
  if y1<0:
    for i in range(21):
      capp(spawn(x+i,y))
  res+=dealmvmp(mp,bd,x,y)
  return mp,x,y,res
def hitest(x,y,mp):
  for i in mp:
    if i.x==x+10 and i.y==y+3:
      return i

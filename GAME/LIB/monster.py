from random import randint as rd,random,choice
from LIB.mapelem import syb,barr
from LIB.sav import gitem,aditem
class mob(syb):
  atk=5
  hp=hpmax=20
  t="m"
  coold=0
  froz=0
  def __init__(s,x,y):
    super().__init__(x,y)
    s.spd=rd(1,5)/10+0.5
  def mvact(s,mp,bd,x,y):
    if s.froz:
      s.froz-=1;return
    if s.coold:
      s.coold-=1
    else:
      s.t="m"
    if random()<=s.spd:
      dx,dy=x+10-s.x,y+3-s.y
      if random()<0.5:
        s.x+=int(dx/abs(dx or 1))
      else:
        s.y+=int(dy/abs(dy or 1))
    for i in mp:
      if isinstance(i,barr) and i.x==s.x and i.y==s.y:
        s.hp-=rd(3,6)
        s.t="x"
        s.coold=2
        if s.hp<=0:
          r=s.drop(bd)
          if r:input(r)
          if s in mp:mp.remove(s)
  def drop(s,bd):
    if random()>0.4:
      r=choice((1,1,2,2,3,3,3))
      if r==1:
        bd["key2"]+=1;return"drp 1*ironkey!"
      elif r==2:
        bd["key1"]+=1;return"drp 1*woodkey!"
      elif r==3:
        aditem(bd,5);return"drop TNT!"
  def act(s,mp,bd):
    hp,ms,win=mpve(bd["hp"],bd["hpmax"],5,5,s)
    if hp==0:
      bd["hp"]=0
      return
    elif win:
      mp.remove(ms)
      bd["hp"]=hp
      return ms.drop(bd)
def getatk(a):
  return (1,4,9,13,15)[a]
def getdef(a):
  return (0,2,5,8,12)[a]
def mpve(hp,hpmax,patk,pdef,ms):
  mshp=ms.hp
  while mshp>0:
    _prgs(hp,hpmax,ms,mshp)
    act=input("ACT: ")
    mshp-=patk
    if mshp<=0:
      break
    _prgs(hp,hpmax,ms,mshp)
    act=input("ACT2: ")
    hp-=ms.atk**2/(ms.atk+pdef)
    if hp<=0:
      print("You died..")
      input()
      hp=0
      break
  return hp,ms,mshp<=0
def _prgs(hp,hpmax,ms,mshp):
  print("\n\n\nM: %d/%d m:%d/%d"%(hp,hpmax,mshp,ms.hpmax))
  pgs=round(15*mshp/ms.hp)
  print("m:"+"["+"-"*pgs+" "*(15-pgs)+"]")
  pgs=round(15*hp/hpmax)
  print("M:"+"["+"-"*pgs+" "*(15-pgs)+"]")
from random import randint as rd,choice
from LIB.sav import gitem,aditem
class syb:
  t="!"
  act=None
  def __init__(s,x,y):
    s.x,s.y=x,y
class schar:
  def __init__(s,x,y,t):
    s.x,s.y,s.t,s.cd,s.act=x,y,t,2,None
  def mvact(s,mp,bd,x,y):
    if s.cd:s.cd-=1;return
    mp.remove(s)
class money(syb):
  t="$"
  def act(s,mp,bd):
    mp.remove(s)
    r=rd(1,3)
    bd["money"]+=r
    return"+%dGold(%d)! "%(r,bd["money"])
class bush(syb):
  t="*"
  sc=False
  def act(s,mp,bd):
    if s.sc:return
    s.sc=True
    hrt=0
    if rd(1,10)>6:
      hrt=rd(0,8)
      bd["hp"]=max(0,bd["hp"]-hrt)
    if hrt:input("Ouch! -%dHP"%hrt)
    chc=rd(1,35)
    if chc in range(1,8):r=rd(1,5);bd["money"]+=r;return"Pick up $%d"%r
    elif chc in range(8,20):aditem(bd,2);return"Pick up berry*1"
    else:return"An usual bush."
class barr(syb):
  t="#"
class tnt(syb):
  t="Q"
  d=5
  def mvact(s,mp,bd,x,y):
    t=[]
    if s.d:s.d-=1;return
    for i in mp.copy():
      if i.__qualname__=="mob":
        if(i.x-s.x)**2+(i.y-s.y)**2<=32:
          r=i.drop(bd)
          if r:t.append(r)
          mp.remove(i)
        elif (i.x-s.x)**2+(i.y-s.y)**2<=81:
          i.hp-=rd(5,10);i.t="x";i.coold=2;i.froz=4
          if i.hp<=0:t.append(i.drop(bd)or"");mp.remove(i)
      elif isinstance(i,syb)and i.t=="@"and (i.x-s.x)**2+(i.y-s.y)**2<=2:
        r=i.open(mp,bd)
        if r:t.append(r)
      elif isinstance(i,syb)and i.t=="T"and (i.x-s.x)**2+(i.y-s.y)**2<=16:
        r=rd(30,100);bd["money"]+=r;mp.remove(i)
        t.append("Trder drop:$"+str(r))
    hrt=(bd["x"]+10-s.x)**2+(bd["y"]+3-s.y)**2 or 1
    if hrt<=10:
      bd["hp"]=max(0,bd["hp"]-int(40/hrt**0.5))
      t.append("HP-%d (%d/%d)\nYou injured."%(int(40/hrt**0.5),bd["hp"],bd["hpmax"]))
    mp.append(schar(s.x-1,s.y,"B"));mp.append(schar(s.x,s.y,"O"));mp.append(schar(s.x+1,s.y,"M"));
    mp.remove(s);return"\n".join(t)
class trader(syb):
  t="T"
  def __init__(s,x,y):
    super().__init__(x,y)
    s.ps,s.ls=[0]*3,[0]*3
    s.ps[0:3]=rd(5,15),rd(20,45),rd(50,100)
    s.ls[0:3]=rd(3,8),rd(2,6),rd(1,3)
  def act(s,mp,bd):
    print("Welcome to my shop!\n +-+  ($%d)"%bd["money"])
    print(" | |  1.w-key(%d)=$%d "%(s.ls[0],s.ps[0]))
    print(" +-+  2.i-key(%d)=$%d "%(s.ls[1],s.ps[1]))
    print("/| |\\/3.g-key(%d)=$%d "%(s.ls[2],s.ps[2]))
    print(" | |    Buy sth?")
    r=input(" | | (1~3):")
    try:r=int(r)-1;assert r in range(0,3)
    except:return
    if s.ls[r]>0:
      if bd["money"]>s.ps[r]:
        bd["money"]-=s.ps[r]
        bd["key%d"%(r+1)]+=1
        s.ls[r]-=1
        return"Buy "+"WIG"[r]+"-key!"
      else:return"Not engh $$!"
    else:return"Not engh goods!"
class box(syb):
  t="@"
  def __init__(s,x,y):
    super().__init__(x,y)
    s.lvl=choice([1,1,1,1,1,1,1,1,2,2,2,2,2,3,3])
  def act(s,mp,bd):
    print("\n     +---------+")
    print("     +---[%d]---+"%s.lvl)
    print("     |  Chest  |\n     |         |")
    print("     +---------+")
    r=input("Use key[1~3]: ")
    try:r=int(r);assert r in range(1,4)
    except:return
    if bd["key"+str(r)]>0:
      bd["key"+str(r)]-=1
      if not rd(1,max(1,4**(s.lvl-r)))==1:input("Key broke!");return
    else:input("No key!(%d/%d/%d)"%(bd["key1"],bd["key2"],bd["key3"]));return
    return s.open(mp,bd)
  def open(s,mp,bd):
    d=choice(((1,2,3),(4,5,6),(7,))[s.lvl-1])
    mp.remove(s)
    if d==1:aditem(bd,3,2);return "redMED+2!"
    elif d==2:aditem(bd,4,2);return "blueMED+1!"
    elif d==3:bd["key2"]+=1;return "ironkey recv!"
    elif d==4:bd["key2"]+=3;return "ironkey*3 recv"
    elif d==5:bd["key3"]+=1;return "goldkey recv!"
    elif d==6:aditem(bd,5,rd(2,5));return"Get TNT!"
    elif d==7:
      m=rd(80,120)
      bd["money"]+=m;return "+%d Gold!(%d)"%(m,bd["money"])
    else:bd["money"]+=100;return "+100g!(%d)"%bd["money"]

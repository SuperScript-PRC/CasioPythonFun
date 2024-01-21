from LIB.mapelem import *
from LIB.sav import gitem
from random import randint as rd,choice
def use(mp,bd):
  if not gitem(bd,5):aditem(bd,5)
  if not gitem(bd,4):aditem(bd,4)
  hpp=round(bd["hp"]/bd["hpmax"]*10)
  print("["+"="*hpp+" "*(10-hpp)+"] %d/%d"%(bd["hp"],bd["hpmax"]))
  print("Keys: %d,%d,%d $%d"%(bd["key1"],bd["key2"],bd["key3"],bd["money"]))
  print("1.Rmed(%d) 3.berry(%d)"%(gitem(bd,3),gitem(bd,2)))
  print("2.Bmed(%d) 4.TNT(%d)"%(gitem(bd,4),gitem(bd,5)))
  r=input("select: ")
  if r=="1"and gitem(bd,3)>0:
      bd["hp"]=min(bd["hp"]+25,bd["hpmax"]);aditem(bd,3,-1)
      return"HP+25(%d/%d)"%(
      bd["hp"],bd["hpmax"])
  elif r=="3"and gitem(bd,2)>0:
    r=rd(2,6)
    bd["hp"]=min(bd["hp"]+r,bd["hpmax"]);aditem(bd,2,-1)
    return"HP+%d(%d/%d)"%(
      r,bd["hp"],bd["hpmax"])
  elif r=="2"and gitem(bd,4)>0:
    for i in mp:
      if i.t=="m":
        i.froz=rd(8,14)
    aditem(bd,4,-1)
    return"FreezeMonster! "
  elif r=="4"and gitem(bd,5)>0:
    aditem(bd,5,-1)
    mp.append(tnt(bd["x"]+10,bd["y"]+3));return"TNT placed."
  return"use nothing"

#print("Low Power")
#raise SystemExit
from random import *
from WuJiang import grps
chous=0
p6,p5,p4=0,0,0
p6st,p5st,p4st=0,0,0
def chou():
  global chous
  res=[]
  for i in range(10):
    chous+=1
    r=randint(1,20000)
    for (m1,m2),star,wj in grps:
      if r in range(m1,m2):
        chk(star)
        cwj=choice(wj)
        res.append("[%d]"%star+cwj)
        if "BaoZhu" in cwj:
          raise Exception("BaoZhu*666! chou:"+str(chous))   
        break
    else:
      res.append("[3]")
  return res
def chk(s):
  global chous,p6st,p5st,p4st,p6,p5,p4
  if s==4:
    p4+=1
    p4st=chous
  elif s==5:
    p5+=1
    p5st=chous
  elif s==6:
    p6+=1
    p6st=chous
def pprint(lst):
  if len(lst)>10:
    print(len(lst))
    raise SystemExit
  print("/".join(lst[0:3]))
  print("/".join(lst[3:6]))
  print("/".join(lst[6:9]))
  print(lst[9])
try:
  while 1:
    try:
      i=int(input() or 1)
    except ValueError:
      i=1
    if i<10:
      for _ in range(i):
        c=chou()
        pprint(c)
    else:
      for _ in range(i):c=chou()
except KeyboardInterrupt:
  print(
  "C:",chous," ",
  "[6]:",int(p6st/p6)if p6>0 else 0,"\n",
  "[5]:",int(p5st/p5)if p5>0 else 0," ",
  "[4]:",int(p4st/p4)if p4>0 else 0,
  sep="")
except Exception as err:
  print(err)
#print("Low Power")
#raise SystemExit
from random import *
from gcani import ani
from lvchts import *
upchi=("NaWeiLaiTe","DanHeng:Immortal Lunae")
chous=0
ups=0
qups=0
p5st=0
q5st=0
p4st=0
q4st=0
bd10=0
xbd=0
xbdpc=xbdpc0=6
dbd=False
chou=500
enableBaodi=True
print("\n\n\nGenshin Gacha!------")
def cka1():
  global dbd,xbd,xbdpc,bd10,chou,chous,ups,p5st,p4st,qups,q5st,q4st
  chou-=1
  chous+=1
  if randint(1,1000)<xbdpc:
    xbdpc=xbdpc0
    xbd=0
    p5st+=1
    q5st=chous
    if randint(0,1) or (dbd and enableBaodi):
      dbd=False
      ups+=1
      qups=chous
      return "[5]"+choice(upchi)
    elif enableBaodi:
      dbd=True
    return "[5]"+choice(czchi5s)
  xbd+=1
  if xbd>75 and enableBaodi:
    xbdpc+=50
  bd10+=1
  if bd10>=10 or randint(1,20)<2:
    bd10=0
    p4st+=1
    q4st=chous
    return "[4]"+choice(czchi4s)
  else:
    return "[3]..."
def cka10():
  txt=""
  for _ in range(3):
    txt+="\n"+"/".join([cka1() for _ in range(3)]).replace(".","")
  txt+="\n"+cka1().replace(".","")
  return txt
while 1:
 try:
  print("chou shu:",chou,"/ 500")
  print("1Chou=1,",end="")
  print("10Lian=2")
  resp=input("1~2:")
  if resp=="1":
    ani()
    print("-Genshin-Gacha-------")
    print(cka1())
  elif resp=="X":
    enableBaodi=False
  else:
    ani()
    print(cka10())
 except KeyboardInterrupt:
   print("1up:",int(qups/ups if ups>0 else 0),
   "[5]:"+str(int(q5st/p5st if p5st>0 else 0)),
   "[4]:"+str(int(q4st/p4st if p4st>0 else 0)))
   break
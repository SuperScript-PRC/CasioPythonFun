from LIB.lda import loading
loading("Loading save..")
from LIB.sav import pwd,aditem
loading("Loading pwd..")
from LIB.cod import load,dump,ginit
from LIB.map import move,hitest,drawmap,use
from random import choice
class X:
  __repr__=lambda _:XXX()
if input("New[input/EXE]? "):
  bdic=pwd()
else:
  bdic=ginit()
  aditem(bdic,5)
map=[]
x,y=bdic["x"],bdic["y"]
cmd,cmdts,ntleft="",[],0
ipwd=""
def XXX():
 global bdic,ipwd,ntleft,cmd,cmdt,cmdts,map,x,y
 if ipwd:
   bdic=pwd(ipwd)
 try:
  while 1:
   drawmap(map,x,y)
   if ntleft>0 or cmdts:
    if cmdts:
      ntleft=2
      cmdt=cmdts.pop()
    else:
      ntleft-=1
   else:
    cmdt="x:%d,y:%d"%(x,y)
   cmd=input(cmdt+" ") or cmd
   if cmd in list("8426"):
    if cmd=="8":c=(0,-1)
    elif cmd=="2":c=(0,1)
    elif cmd=="4":c=(-1,0)
    elif cmd=="6":c=(1,0)
    map,x,y,r=move(x,y,map,bdic,c[0],c[1])
    cmdts+=r
   elif cmd==".":
    ntleft=2;cmdts.append(use(map,bdic));cmd=""
   sth=hitest(x,y,map)
   if sth and sth.act:
    r=sth.act(map,bdic)
    if r:
      cmdts.append(r)
   if bdic["hp"]<=0:
    print("You died...")
    break
   bdic["x"],bdic["y"]=x,y
 except KeyboardInterrupt:
   print(dump(bdic))
 finally:
   globals()["bdic"]["hp"]=100
   ipwd=dump(bdic)
X=X()
X.__repr__()
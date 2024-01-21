from casioplot import *
from random import *
psec=4
tis=20
rng=(-100,100)
psco=0
nsco=0
cuotis=[]
op=lambda a,b:a+b
def sp(t):
  for i in range(int(5000*t)):
    show_screen()   
def genexp(a,b):
  right=choice((0,1))
  if b>=0:
    txt="{}+{}={}"
  else:
    txt="{}{}={}"
  if right:
    ans=op(a,b)
  else:
    ans=[i for i in str(a+b)]
    pos=randint(0,len(ans)-1)
    if a+b<0 and not pos:pos+=1
    ans[pos]=str(int(ans[pos])-choice([-1,1])).replace("-","")
    ans=int("".join(ans))
  return txt.format(a,b,ans),right
def ctcoll(gen,ans,r=0):
  cuotis.append(gen+" yes" if r else gen+" X "+str(ans))
def djs(c,t):
  c=round(20*c/t)
  clear_screen()
  draw_string(35,1,"<"+"="*c+"-"*(20-c)+">")
def tm(t):
  global psco,nsco
  a=randint(*rng)
  b=randint(*rng)
  que,right=genexp(a,b)
  clear_screen()
  try:
   for i in range(psec*50):
     djs(psec*50-i,psec*50)
     draw_string(1,1,"{}/{}".format(t,tis),(0,0,0),"large")
     draw_string(20,25,que+" ?",(0,0,0),"large")
     #draw_string(1,50,str(bool(right)))
     for i in range(200):
       show_screen()
   if not right:
     psco+=1
   else:
     ctcoll(que,op(a,b),1)
     nsco+=1
  except KeyboardInterrupt:
    if right:
      psco+=1
    else:
      nsco+=1
      ctcoll(que,op(a,b))
print("\n\n\n\n-------correct-------")
for i in range(tis):
  tm(i+1)
clear_screen()
for i in cuotis:
  print(i)
try:
 draw_string(0,0,"Ok!!",(0,0,0),"large")
 sp(2)
 draw_string(0,15,"right: "+str(psco),(0,0,0),"large")
 sp(2)
 draw_string(0,30,"wrong: "+str(nsco),(0,0,0),"large")
 sp(2)
 while 1:
  draw_string(0,45,"Press [AC]",(0,0,0),"large")
  sp(2)
  draw_string(0,45,"Press [AC]",(255,255,255),"large")
  sp(2)
except:
  raise SystemExit
cl="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-"
def ecn(t):
  s=0
  for i in range(0,len(t)):
    s+=cl.find(t[i])*len(cl)**(len(t)-1-i)
  return s
def ect(n,mins=1):
  s=""
  while n>0:
    n,b=divmod(n,len(cl))
    s=cl[int(b)]+s
  return "0"*(mins-len(s))+s if len(s)<mins else s
def bitsplit(n,mins=1):
  s=bin(n)[2:]
  return "0"*(mins-len(s))+s
def load(t):
  mp={}
  mp["x"]=ecn(t[3:6])-2177
  mp["y"]=ecn(t[6:9])-2177
  mp["map"]=ecn(t[9:12])
  mp["hp"]=ecn(t[12:14])
  mp["hpmax"]=ecn(t[14:16])
  mp["key"]=ecn(t[16:19])
  mp["daoju"]=ecn(t[19:21])
  mp["money"]=ecn(t[21:23])
  mp["others"]=t[23:36]
  rddetail(mp)
  return mp
def dump(mp):
  dpdetail(mp)
  t=(ect(mp["x"]+2177,3)+ect(mp["y"]+2177,3)+ect(mp["map"],3)+ect(mp["hp"],2)
  +ect(mp["hpmax"],2)+ect(mp["key"],3)
  +ect(mp["daoju"],2)+ect(mp["money"],2)+mp["others"])
  return ect(hash(t),3)+t
def rddetail(mp):
  c=bitsplit(mp["key"],18)
  mp["key1"]=int(c[0:6],2)
  mp["key2"]=int(c[6:12],2)
  mp["key3"]=int(c[12:18],2)
  c=""
  for i in mp["others"]:
    c+=bitsplit(ecn(i),6)
  mp["extras"]={}
  for i in range(0,len(c),9):
    iid=int(c[i:i+4],2)
    icnt=int(c[i+4:i+9],2)
    mp["extras"][iid]=icnt
def dpdetail(mp):
  mp["key"]=mp["key1"]*4096+mp["key2"]*64+mp["key3"]
  ot=""
  for i,j in mp["extras"].items():
    ot+=bitsplit(i,4)+bitsplit(j,5)
  mp["others"]=ect(int(ot or "0",2),12)
def ginit(n={0:0}):
  r={"x":0,"y":0,"map":99,
  "hp":100,"hpmax":100,
  "key":4161,"daoju":0,
  "money":100,"others":"0"}
  rddetail(r);r["extras"]=n
  return r
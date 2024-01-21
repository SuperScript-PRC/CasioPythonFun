try:
  from LIB.chemlist import *
  from LIB.chempars import *
except:
  from chemlist import *
  from chempars import *
KEYS=["+","-","=","*"]
def elecpbs(x1):
  mp=elecmapstr.split(",")
  pnt,fn,x=0,[],x1
  while x>0:
    pnt+=1
    sc,tc=mp[pnt-1]
    td={"s":2,"p":6,"d":10,"f":14}[tc]
    if x-td>=0:
      fn.append(str(sc)+tc+str(td))
      x-=td
    else:
      fn.append(str(sc)+tc+str(x))
      x=0
  if x1 in specelecpbs.keys():
    fn=fn[:-3]+specelecpbs[x1]
  return chsort(fn),x1 in specelecpbs.keys()
def xdfzzl(sb):
  def o(s):
    synt,sum="",0
    for i0 in s:
      if i0 in KEYS:continue
      i,j=i0
      if isinstance(i,list):
        r,s=o(i)
        s="("+s+")"
      else:
        r=elems.get(i,(0,float("nan")))[1]
        s=str(r)
      sum+=r*j
      synt+="+"+s+(""if j==1 else "*"+str(j))
    return sum,synt[1:]
  r,s=o(sb)
  t=((s or "Empty")+"=%.1f"%r).replace("nan","?")
  if len(t)>42:input("[Continue]")
  pprint(t)
def showyzzl(y,dbg=False,o=""):
  d={}
  dd=elems
  for i0 in y:
    if i0 in KEYS:continue
    i,_=i0
    if isinstance(i,list):
      d.update(showyzzl(i,True))
    elif i not in d:
      d[i]=elems.get(i,(0,float("nan")))[1]
  if dbg:return d
  else:
    s=0
    if len(o)>18:
      o=o[:16]+".."
    print(o+"-"*max(21-len(o),0))
    for i,j in d.items():
      s+=1
      if not s%12:input()
      elif not s%3:print()
      print("{}={} ".format(i,j).replace("nan","?"),end="")
    print("\n"+"-"*21)
def pprint(l):
  for i in range(0,len(l),21):
    print(l[i:i+21])
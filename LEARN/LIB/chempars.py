synterr=SyntaxError("Syntax ERROR")
def chem_pars(sub):
  cname,cnum,cma,cmat="","",0,""
  flb=[]
  for i in sub+"E":
    if i=="(":
      cma+=1
      if cname:
        flb.append((cname,int(cnum or 1)))
        cname=""
      cnum=""
    elif i==")":
      cma-=1
      if not cma:
        cname=chem_pars(cmat[1:])
        cmat=""
      if not cma and not cname:
        raise SyntaxError("Empty comma")
    if not cma:
      if ord(i) in range(65,91):
        if cname:
          flb.append((cname,int(cnum or 1)))
        cname,cnum=i,""
      elif ord(i) in range(97,123):
        if not cname:raise SyntaxError("Empty Comma or atom")
        elif ord(cname[-1]) in range(97,123):raise SyntaxError("Not a valid atom")
        cname+=i
      elif ord(i) in range(48,58):
        cnum+=i
      elif i in "+=-*":
        if cname:
          flb.append((cname,cnum or 1))
          cname,cnum="",0
        flb.append(i)
      elif i!=")":
        raise SyntaxError("Invalid char: "+i)
    else:
      cmat+=i
  if cma:
    raise SyntaxError("Comma not closed")
  return flb
def chsort(fn):
  sr=lambda x:x[0]+{"s":"1","p":"2","d":"3","f":"4"}[x[1]]
  fn.sort(key=sr)
  return fn
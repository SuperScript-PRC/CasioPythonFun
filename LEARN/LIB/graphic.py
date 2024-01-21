gpu=lambda :[[" "for j in range(21)]for i in range(7)]
class sybl:
  def __init__(s,b,x,y):
    s.b=b
    s.x,s.y=x,y
  def showxy(s,x,y):
    dx=s.x-x
    dy=s.y-y
    if dx in range(0,21) and dy in range(0,7):
      return dx,dy
    return None
def unfold(w,fx=0,fy=0,exx=1,exy=1):
  cname=""
  gpc=[]
  app=lambda t,x,y:gpc.append(sybl(t,x,y))
  def glen(s):return len(s.b)
  for i in w:
    if len(i)==1:
      app(i,fx,fy)
      fx+=exx
    elif isinstance(i[0],list):
      if i[0][0] in ["+","-","="]:
        app(i[0][0],fx-exx,fy+exy)
        gpc+=unfold(i[0][1:],fx-exx,fy+exy*2,exx,exy)
      else:
        app("|",fx-exx,fy+exy)
        gpc+=unfold(i[0],fx-exx,fy+exy*2,exx,exy)
    else:
      app(i[0][0],fx,fy)
      fx+=exx
      if len(i[0])-1:
        app(i[0][1],fx,fy)
        fx+=exx
      if i[1]-1:
        app(str(i[1]),fx,fy)
        fx+=exx
  return gpc
def show(l):
  for i in l:
    print("".join(i))
def move(s):
  prompt=1
  lastcmd=""
  nx,ny=0,0
  try:
   while 1:
    g1=gpu()
    for i in s:
      j=i.showxy(nx,ny)
      if j:
        x,y=j
        g1[y][x]=i.b
    show(g1[:6])
    lastcmd=input("".join(g1[6])) or lastcmd
    if lastcmd=="8":ny-=1
    elif lastcmd=="6":nx+=1
    elif lastcmd=="2":ny+=1
    elif lastcmd=="4":nx-=1
  except KeyboardInterrupt:
    pass
from LIB.gzp import *
crs=[]
def showfmer(lst):
  for i in range(len(lst)):
    print("%.2d> "%(i+1)+lst[i])
def edt(jp):
  assert jp in range(1,len(crs)+1)
  print("Edit=========")
  showfmer(crs[:jp-1])
  new=input("%.2d> "%jp) or "0"
  crs[jp-1]=new
  showsuc()
def showsuc():
  clear_screen()
  crs1=" ".join(ect(int("0b"+(i)),2) for i in crs)
  print("EditOff=======")
  print(crs1[:15])
  print(crs1[15:])
  drawchr(0,0,crs1)
  show_screen()
  print("edt()")
  print("to edit again.")
print("Character Maker")
print("Press [AC] to stop.")
while 1:
  print("[01]=========")
  try:
    i=1
    while i<11:
      inp=input("%.2d> "%i) or "0"
      if inp.startswith("2"):
        try:
          print("Edit=========")
          jp=int(inp[1:])
          showfmer(crs[:jp-1])
          new=input("%.2d> "%jp) or "0"
          crs[jp-1]=new
          print("EditOK=======")
          showfmer(crs[:i])
          continue
        except ValueError:
          print("value error")
          continue
        except IndexError:
          print("index wrong")
          continue
      crs.append(inp)
      i+=1
    break
  except KeyboardInterrupt:
    try:
      print("[AC]exit [EXE]remake")
      input()
    except KeyboardInterrupt:
      raise SystemExit
showsuc()
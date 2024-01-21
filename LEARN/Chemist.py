from LIB.chemlist import *
print(" +-----------------+")
print(" |  HuaXue(Chems)  |")
print(" |  SuperScript    |")
print(" |  welcome :D     |")
print(" |    --2023.12.6  |")
print(" +-----------------+")
try:
 while 1:
  sel=input("[Continue]")
  print("[1] Mass of Matter")
  print("[2] Electronic Sort")
  print("[3] Structure Image")
  print()
  print()
  print()
  if not sel:
    sel=input("Select> ")
  if sel=="1":
   from LIB.cpu import *
   matt=input("Matter: ")
   try:
     s=chem_pars(matt)
     showyzzl(s,o=matt)
     xdfzzl(s)
   except SyntaxError as err:
     print(err)
  elif sel=="2":
   from LIB.cpu import *
   s0=input("Atom: ")
   s=elems.get(s0,0)
   if not s:
     print("Not exists")
   else:
     print("-"*21+"\n"+s0+": {}, M({})={}".format(s[0],s0,s[1]))
     s,s0=elecpbs(s[0])
     pprint("|".join(s)+("\n(Special)"if s0 else ""))
  elif sel=="3":
    from LIB.graphic import *
    from LIB.chempars import *
    try:
      s=chem_pars(input("Matter:") or "O(C(O-CH3)=O)-CH3")
      print("TIPS------------------\nType 8/4/6/2\nto move screen.")
      input("[ok]")
      move(unfold(s))
    except SyntaxError as err:
      print(err)
except KeyboardInterrupt:
  pass
from random import randint
try:
  from LIB.cod import ecn,load
except ImportError:
  from cod import ecn,load
def gitem(bdic,it):
  return bdic["extras"].get(it,0)
def aditem(bdic,it,c=1):
  bdic["extras"][it]=bdic["extras"].get(it,0)+c
def pwd(pw=""):
  while 1:
   code=pw or input("Save code:")
   if len(code)<29:
     print("too short:",len(code))
     pw=""
   elif hash(code[3:])!=ecn(code[0:3]):
     print("wrong password")
     pw=""
   else:
     return load(code)
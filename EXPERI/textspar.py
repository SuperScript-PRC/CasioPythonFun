from LIB.gzp import *
from LIB.chars import *
def sp1():
  drawchr(25,20,chrs["yuan2"])
  drawchr(35,20,chrs["shen2"])
def sp2():
  drawchr(45,20,chrs["qi3"])
  drawchr(55,20,chrs["dong4"])
i=0
while 1:
  i+=1
  clear_screen()
  if i%2==0:
    sp1()
  else:
    sp2()
  for j in range(2000):
    show_screen()
    
  
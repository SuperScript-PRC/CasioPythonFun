from casioplot import show_screen,draw_string,clear_screen
def loading(txt):
  clear_screen()
  draw_string(20,26,txt,(0,0,0),"large")
  for i in range(1000):
    show_screen()
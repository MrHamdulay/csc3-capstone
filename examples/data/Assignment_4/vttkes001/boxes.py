"""
    print_square (), that prints a 5x5 box on the screen
    print_rectangle (width, height), that prints a box on the screen with given width and height
    get_rectangle (width, height) that returns a string containing a box with given width and height
"""
def print_square():
  print("*****")
  print("*   *")
  print("*   *")
  print("*   *")
  print("*****")
  
def print_rectangle1(width,height):

  forloop = ""
  for i in range(height - 2):
    forloop = forloop +("*" + (width - 2) *" " + "*" + "\n")
  boxy = (width *"*" + "\n" + forloop + width *"*")
  return boxy

def print_rectangle(width,height):
  forloop = ""
  for i in range(height - 2):
    forloop = forloop +("*" + (width - 2) *" " + "*" + "\n")
  boxy = (width *"*" + "\n" + forloop + width *"*")
  print (boxy)
  
   
def get_rectangle(width,height):
  box = print_rectangle1(width,height)
  return box    


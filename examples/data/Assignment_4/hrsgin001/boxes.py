def print_square ():
  print("*****")
  for i in range (3):
    print("*", " "*3, "*", sep = "")
  print("*****")
  
def print_rectangle (width, height):
  print("*"*width)
  for i in range (1, height-1):
    print("*", " "*(width-2), "*", sep = "")
  print("*"*width)

def get_rectangle (width, height):
  x = ("*"*width)
  x+="\n"
  for i in range (1, height-1):
    x += "*"
    x+= " "*(width-2)
    x+= "*\n"
  x+=("*"*width)
  return x
    
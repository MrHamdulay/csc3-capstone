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
 
 

    
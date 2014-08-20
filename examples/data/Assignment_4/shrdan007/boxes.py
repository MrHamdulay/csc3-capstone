def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*" + (" "*(width-2)) + "*")
    print("*"*width)
    
def get_rectangle(width, height):
  y = str("*"*width)
  x = str("*" + (" "*(width-2)) + "*" + "\n")
  z = str((height-2)*x)
  return y + '\n' + z + y
         
         

  
   
    
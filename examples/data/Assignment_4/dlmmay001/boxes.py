def print_square ():
   char = "*"
   space = ' '
   print(char*5)
   for i in range(3):
      print(char,space,char)
   print(char*5)
   

def print_rectangle (width, height):
   char = "*"
   space = ' '
   print(char*int(width))
   for i in range(height-2):
      print(char,space*(width-2),char,sep='')
   print(char*int(width))
   
def get_rectangle (width, height):
   char = "*"
   space = ' '
   print(char*int(width))
   for i in range(height-2):
      print(char,space*(width-2),char,sep='')
   print(char*int(width))   
   
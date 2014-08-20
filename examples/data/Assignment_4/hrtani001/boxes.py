def print_rectangle(width, height):
   print("*"*width)
   for j in range(0,height-2):
      print("*"," "*(width-2), "*", sep="")
   print("*"*width)
   
def print_square():
   print_rectangle(5,5)
   
def get_rectangle(width,height):
   st=("*"*width)
   for i in range(0, height-2):
      st+= "\n*"+(" "*(width-2))+"*"
   st+="\n"+"*"*width
   return st
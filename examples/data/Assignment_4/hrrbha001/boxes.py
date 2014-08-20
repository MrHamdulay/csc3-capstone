def print_square():
   print ("*****")
   print ("*   *")
   print ("*   *")
   print ("*   *")
   print ("*****")
   
def print_rectangle (width, height):
   for i in range (width):
      print ("*",end="")
   print ()   
   for i in range (height-2):
      print ("*",end="")
      for i in range (width-2):
         print (" ", end="")
      print ("*")
   for i in range (width):
      print ("*",end="")
   print ()   
    
def get_rectangle (width, height):
   output = ""
   for i in range (width):
      output = output + "*"
   output = output + "\n"
   for i in range (height-2):
      output = output + "*"
      for i in range (width-2):
         output = output + " "
      output = output + "*\n"
   for i in range (width):
      output = output + "*"
   return output


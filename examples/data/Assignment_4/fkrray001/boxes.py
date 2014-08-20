# Author : Rayaan Fakier FKRRAY001
# Date : 28 - 03 - 2014

def print_square ():
   print("*" * 5)
   for j in range(3): # Prints mid-section thrice
      print("*" + " " * 3 + "*")
   print("*" * 5)
   
def print_rectangle(width, height):
   print("*" * width)
   k = 0
   while k < height - 2: 
      print("*" + " " * (width - 2) + "*") # Print mid-section according to height
      k += 1
   print("*" * width)

def get_rectangle(width, height):
   rect = "*" * width
   s = 0
   rect+="\n"
   while s < height - 2: 
         rect+= "*" + " " * (width - 2) + "*" + "\n"
         s += 1
   rect+="*" * width
   return rect
      
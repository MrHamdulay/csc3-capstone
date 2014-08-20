def print_square():
   for i in range(5): 
      if i == 0 or i ==4: 
         print("*****")
      else:
         print("*   *") 
def print_rectangle(width,height):
   for i in range (height):
      if i == 0 or i == (height-1):
         print("*"*width)
      else:
         print("*" + (" "*(width-2))+ ("*"))
def get_rectangle(width,height):
   box = "";  
   for i in range (height):
      if i == 0 or i == (height-1):
         box = box +("*"*width + "\n")
      else:
         box = box +("*" + (" "*(width-2))+ ("*") + "\n")
   return box    




    
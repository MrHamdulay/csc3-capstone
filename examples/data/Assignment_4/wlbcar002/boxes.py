def print_square():
   for i in range(5):
      if i == 0 or i==4:
         print('*****')
      else:
         print('*'," "*(3),'*',sep="")
    
 
def print_rectangle (width, height):
   for i in range(height):
      if i == 0 or i == height-1:
         print('*'*width)
      else:
         print('*'," "*(width-2),'*',sep="")
  
def get_rectangle (width, height):
   square = ""
   for i in range(height):
      if i == 0:
         square +='*'*width+'\n'
      if 0<i<height-1:
         square += '*'+" "*(width-2)+"*\n"
      if i == height-1:
         square +='*'*width
   return (square)



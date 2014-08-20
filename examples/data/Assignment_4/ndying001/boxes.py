def print_square():
   width=5
   height=5
   space=width-2
   print('*'*width)
   for i in range(height-2):
      print('*'," "*space,'*',sep="")
   print('*'*width)
def print_rectangle(width,height):
   space=width-2
   print('*'*width)
   for i in range(height-2):
      print('*'," "*space,'*',sep="")
   print('*'*width)
def get_rectangle(width,height):
   space=width-2
   r='*'*width
   for i in range (height-2):
      r+='\n'+'*'+' '*space+'*'
   r+='\n'+'*'*width
   return r
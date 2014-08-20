def print_square():
   width1=5
   height1=5
   space=width1-2
   print('*'*width1)
   for i in range(height1-2):
      print('*'," "*space,'*',sep="")
   print('*'*width1)
def print_rectangle(width1,height1):
   space=width1-2
   print('*'*width1)
   for i in range(height1-2):
      print('*'," "*space,'*',sep="")
   print('*'*width1)
def get_rectangle(width1,height1):
   space=width1-2
   k='*'*width1
   for i in range (height1-2):
      k+='\n'+'*'+' '*space+'*'
   k+='\n'+'*'*width1
   return k
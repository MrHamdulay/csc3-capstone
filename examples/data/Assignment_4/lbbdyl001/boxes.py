def print_square(size=5):
   inner_size=size-2
   print('*'*size)
   for i in range(inner_size):
      print ('*' + ' ' * inner_size + '*')
   print ('*' * size)   
      

def print_rectangle(width,height):
   for i in range(height):
         for j in range(width):
            print('*' if i in [0, height-1] or j in [0, width-1] else ' ', end='')
         print()

def get_rectangle(e,f):
   for i in range(f):
      for j in range(e):
         print('*' if i in [0, f-1] or j in [0, e-1] else ' ', end='')
      
      
            


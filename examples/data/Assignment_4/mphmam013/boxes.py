def print_square():
    print('*'*5)
    for i in range(3):
        print('*',' '*3,'*',sep='')
    print('*'*5)


def print_rectangle(width,height):
    y=width-2
    z=height-2
    print('*'*width)
    for i in range(z):
        print('*',' '*y,'*',sep='')
    print('*'*width)
def get_rectangle(width,height):
   space=width-2
   r='*'*width
   for i in range (height-2):
      r+='\n'+'*'+' '*space+'*'
   r+='\n'+'*'*width
   return r
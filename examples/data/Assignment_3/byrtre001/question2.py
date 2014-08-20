def a(height,par2):
     final=height*2
     gap=(final//2)-1
     for i in range(0,final,2):
          print(' '*gap,end='')  
          print(par2*(i+1))
          gap=gap-1 # can also write this as: gap-=1
height=eval(input('Enter the height of the triangle:''\n'))
a(height,'*')
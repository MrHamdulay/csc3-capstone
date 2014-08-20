def equi(height):
     gap=height-1  
     for i in range(1,height+1):
          print(' '*gap,end='')  
          print('*'*((2*i)-1))
          gap=gap-1
height = eval(input("Enter the height of the triangle:\n"))
equi(height)
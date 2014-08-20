def triangle(width,par2):
     gap=width-1
     for i in range(0,width,1):
          print(' '*gap,end='')  
          print(par2*(i+1),end='')
          print(par2*(i))
          gap=gap-1
width=eval(input("Enter the height of the triangle:\n"))
par2="*"
triangle(width,par2)

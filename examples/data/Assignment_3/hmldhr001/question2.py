height=eval(input("Enter the height of the triangle:\n"))
spacing=height-1
j=1

for i in range(height):
     print(' '*spacing,end='')  
     print("*"*(j))
     spacing=spacing-1 
     j+=2
     
   
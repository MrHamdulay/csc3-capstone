height=eval(input("Enter the height of the triangle:\n"))
height = (height*2) - 1
space=height//2
for i in range(0,height,2):
          print(' '*space,end='')  
          print("*"*(i+1))
          space-=1

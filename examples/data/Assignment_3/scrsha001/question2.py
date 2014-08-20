def a():
 x = eval(input("Enter the height of the triangle:\n"))
 y = x*2
 gap=x-1
 for i in range(0,y,2):
  print(" "*gap,end="")
  print("*"*(i+1),sep="")
  gap=gap-1
  
a()
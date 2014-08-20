def tri():

 height = eval(input("Enter the height of the triangle:\n"))

 base = height*2

 gap=height-1

 for i in range(0,base,2):

  print(" "*gap,end="")

  print("*"*(i+1),sep="")

  gap=gap-1

  

tri()
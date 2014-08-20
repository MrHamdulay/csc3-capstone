def triangle():
 
 height = eval(input("Enter the height of the triangle:\n"))
 base = height*2
 space=height-1

 for i in range(0,base,2):

  print(" "*space,end="")

  print("*"*(i+1),sep="")

  space=space-1

  

triangle()
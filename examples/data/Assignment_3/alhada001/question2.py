l = eval(input("Enter the height of the triangle: \n"))
number = (2*l)-1

for i in range(l): 
   if i > 0:
       print(" " * (i-1), number * "*",end="\n")
       number = number - 2
   else:
      print(number * "*",end="\n")
      number = number - 2      
   
      
   

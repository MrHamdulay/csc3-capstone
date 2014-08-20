function = input("Enter a function f(x):\n")
import math
def getfunction(new_x):
   new_x2= str(new_x)
   new_x2= "("+new_x2+")"
   newfunction = function.replace("x", new_x2 )
   finalfunction1=round(eval(newfunction))
   #print (finalfunction1)
   return finalfunction1

def getx():
   x1=0
   for i in range(-10,11):
      x1+=1
def plot():
   #for y in range (-10,11):
   
   for y in range(-10,11):
      
      for x in range(-10,11):
            variable = False 
            if -y == getfunction(x):
               variable = True
         
            if variable:
               print("o",end="")
            elif x==0 and y==0:
               print("+",end="")
            elif y == 0:
               print("-",end="")
            elif x == 0:
               print("|",end="")
            else:
               print(" ",end="")
          
            variable = False
      print()
plot() 
#to test for all values


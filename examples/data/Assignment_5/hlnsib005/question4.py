#Sibulele Hlongwane
#Date: 15 April 2014
#Question 4
#Drawing of Functions

import math

function= input("Enter a function f(x):\n")    #y=x+2
#set range of axis
for y in range(-10,11): 
  # print("|")
   for x in range(-10,11):
      if round(eval(function))==-y:
         print("o",end="")
      else: 
         if (x==0) and (y==0):
            print("+",end="")    
         else:         
         #x axis
            if y==0:
               print("-",end="") 
            else:            
            #y axis
               if x==0:
                  print("|",end="")                  
               else:
               #place holder for empty spaces
                  print(" ", end="")   
   print()#newline
 #  print("|",end="")
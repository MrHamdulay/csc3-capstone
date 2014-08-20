#a program that draws a text-based graph of a mathematical function
#Jenny Luo
#15 april 2014

import math

def main():
   x=0
   f_of_x=input("Enter a function f(x):\n") #get the input as a string from the user

# nested loop to create a grid with the required limits      
   for y in range(10,-11,-1):
      for x in range(-10,11,1):
         if y==round(eval(f_of_x)):     #equalise both sides of the equation
            print("o",end="")
         elif x==0 and y!=0:           #pget the y-axis
            print("|", end="")
         elif y==0 and x!=0:         #get the x-axis
            print("-", end="")
         elif y==0 and x==0:        #get the origin
            print("+", end="")
         else:
            print(" ",end="")       
         
      print()
main()
         
         
      
       

        
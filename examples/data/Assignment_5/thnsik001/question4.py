"""Question4 Assignment5 draws function
Skhulile Thenjwayo
16 April 2014"""
import math
function = (input("Enter a function f(x):\n")).lower()

def func(a,y):
    #calculating x values
   x=a
   if y==-round(eval(function),0):
      return True

def graph():
    #drawing graph
   for y in range(-10,11,1):
      for x in range(-10,11):
         if func(x,y):
            print("o",end="")
         elif x==0 and -y==0:
            print("+",end="")            
         elif y==0: 
            print("-",end="")
         elif x == 0:
            print("|",end="")
         else: print(" ",end="")
      print()
graph()
"""Create a neater math program- Kiara Ramjith- 2014"""
import math
def get_integer (x): #get a parameter
   num=input("Enter "+x+":\n") #get an input using the parameter
   while not num.isdigit(): #while input is not a digit continue asking for input
      num=input("Enter "+x+":\n")
   return eval(num) #return num
def calc_factorial (i): 
   fact= math.factorial(i) # uses the math library to calculate factorial of a number
   return fact
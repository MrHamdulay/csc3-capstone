"""this program calculates the number of k-permutations of n items""" 
# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014
#import string
import math
def get_integer(var): #one function is defined
   
   n = input ("Enter "+var+":\n") #this is asking the user fo the n number
   while not n.isdigit (): #this says why n is not a digit carry on with this loop
      n = input ("Enter "+var+":\n")
   n = eval (n) #this is the point at which end becomes a number   
   return n #n is retured so that it can be used in other prgroam call question 3
   
    
     
def calc_factorial(var): #another function is defined
   factorial = 1 
   for i in range (1, var+1): #this loop is used to make factorial until the maximum number is reached hence the range
      factorial *= i #the factorial is updated each time by multiplying the number value in the range
   return(factorial)
#calc_factorial (var) #calling the function



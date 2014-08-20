""" A module containing functions that calculate the number og k-permutations
Author: Afika Nyati
Date: 15th April 2014"""


def get_integer(name_of_integer): 
   
   integer = "" # Initializing sentinel variable
   
   while not integer.isdigit(): # If the given string input is not an number, it asks the user for a number until it gets one.
      integer = input ("Enter " + name_of_integer + ":\n")
   
   return int(integer) # Converts given output to an integer and returns value




def calc_factorial(number):
   
   result = 1 # Initializing variable
   
   for i in range(1, number + 1): # Multiplies each integer from 1 to the number to calculate its factorial
      result *= i
      
   return result



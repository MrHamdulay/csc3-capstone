'''Write a program that calculates the number of k-permutations of n items by improving given code
Sinead Urisohn
15 April 2014'''

#function to get integer that receives parameter
def get_integer(n):
   #get input from user to enter value
   userInput = input ("Enter "+n+":\n")
   #reask if input not digit
   while not userInput.isdigit ():
      userInput = input ("Enter "+n+":\n")
   #evaluate to number
   userInput= eval (userInput)    
   #return number
   return userInput
#function to calcuate factorial of given parameter number
def calc_factorial(n):
   #set factorial to 1
   nfactorial = 1
   #loop from 1 until and including parameter number
   for i in range (1, n+1):
      #increment factorial to accumalate products based on loop to get factorial
      nfactorial *= i
   #return acummulated factorial
   return nfactorial
    
# calculate number of k-permutations of n items
# Megan Swartz
# 16 april 2014

#define a function to get a random integer
def get_integer (x):
   print("Enter ", x, ":", sep = "")   #input doesn't allow for more than one input, thus a print statement is needed to account for the variable 
   integer_input = input("")
   while not integer_input.isdigit():   #run again until the user enters valid input 
      print("Enter ", x, ":", sep = "")
      integer_input = input("")
   integer_input = eval(integer_input)
   return integer_input    #returns integer for use in question3.py
   
def calc_factorial(y):
   yfactorial = 1    #from original program 
   for i in range (1, y+1):
      yfactorial *= i 
   return yfactorial
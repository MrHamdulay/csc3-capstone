# Refactored and reorganised program to 
# make better use of functions and thereby
# reduce redundancy and improve reusability of code.
# hendrik Joosten
# 17 april 2014

# method to get a integer from the user
def get_integer(user_char):
      # initializing the variable ret_user_int
      ret_user_int = 0
      # setting the variable to the users input, using a changing input meassage
      ret_user_int = input ("Enter " +user_char+ ":\n")
      # checking if the input variable is a digit
      while not ret_user_int.isdigit (): 
            ret_user_int = input ("Enter "+user_char+":\n")
      # evaluating the users input to convert the string to a int
      ret_user_int = eval (ret_user_int)
      # returns the user supplied integer
      return ret_user_int


def calc_factorial(user_integer):
      # initializing the variable factorial to 1
      factorial = 1
      # using a for loop to determine the factorial of user supplied integer
      for i in range (1, user_integer+1):
            factorial = factorial * i
      # returns the factorial of input variable
      return factorial
      
      
      
      


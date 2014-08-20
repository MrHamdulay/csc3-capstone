"""myMath.py - A simple maths module
Keegan Crankshaw
16/04/2014"""

import math

#Get the integer
def get_integer(intName):
    text = ""
    while text.isdigit() == False:
        text = input("Enter " + intName + ":\n")    
    return eval(text)
    
#Calculate the factorial
def calc_factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

if __name__ == "__main__":
   calc_factorial(get_integer("n"))
    
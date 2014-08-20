'''A module that provides generic functions for calculating factorials and permutations'''
### Tashiv Sewpersad
### Assignment 5 - Question 3
### 14 - 04 - 2014

## Declarations
def get_integer(sVar):
  __doc__ = "A function that provides an interface for capturing integers"
  sResult = input("Enter " + sVar + ":\n")
  while not sResult.isdigit():
    sResult = input ("Enter " + sVar + ":\n")
  iResult = eval(sResult)
  return iResult

def calc_factorial(iVal):
  __doc__ = "A function that calculates the factorial of a value provided"
  factorial = 1
  for i in range(1,iVal+1):
    factorial *= i
  return factorial
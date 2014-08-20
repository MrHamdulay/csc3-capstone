#Assignment 3
#Question 4

import math

def is_prime(x):
  for j in range (2,x):
    if (x % j) == 0:
      return False
  return True
            
def palin_prime():
    _min = eval(input("Enter the starting point N: \n")) + 1
    _max = eval(input("Enter the ending point M: \n"))    
    print("The palindromic primes are:")
    for i in range(_min,_max):
        is_prime(i)
        if is_prime(i) == True:
            number1 = str(i)
            number2 = number1[::-1]
            if number1 == number2:
              print(i)
        else:
            continue
            
    

    



palin_prime()
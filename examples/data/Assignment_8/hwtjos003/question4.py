"""palindromic primes
Joshua Hewitson
2/5/2014"""

import sys
import math
sys.setrecursionlimit (30000)

def find_primes(input1, input2):
    # input1 will be greater than input2 when all the numbers have been checked
    if input1 > input2:
        return
    
    # 
    if check_palindrome(str(input1)):
        if is_Prime(input1, 2):
            print(input1)
    find_primes(input1+1,input2)
def is_Prime(input1, count):
    if count > math.sqrt(input1) and input1 > 3:
        return True
    if input1 == 0 or input1 == 1:
        return False
    elif input1 == 2 or input1 == 3:
        return True
    
    if input1 % count == 0:
        return False
        
    else:
        if is_Prime(input1, count+1):
            return True    
        
def check_palindrome(input1):
    # input1 is shortened each time so if it is empty then the whole palindrome has been checked and it is a palindrome
    if input1 == "":
        return True
    
    # each end is checked to be the same, if they are, it passes to the next recursion
    if input1[0] == input1[-1]:
        # input is shortened by removing the end characters
        input1 = input1[1:len(input1)-1]
        # check_palindrome is now run again with a shortened input
        if check_palindrome(input1):
            return True
    
    return False


val1 = eval(input("Enter the starting point N:\n"))
val2 = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
find_primes(val1, val2)
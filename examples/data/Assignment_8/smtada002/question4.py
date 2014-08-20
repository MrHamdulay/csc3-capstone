'''Assignment 8 question 4 palindromic primes
Adam Smith
5 May 2014'''

import math
import sys
sys.setrecursionlimit (30000)

def Prime_Checker(Num, i):#checks if a number is devisible by any int between 1 and itself using recursion
    if Num == 1:
        return False
    elif Num == 2:
        return True
    elif (Num/2).is_integer():
        return False
    elif i >= int(math.sqrt(Num))+1:
        return True    
    elif (Num/i).is_integer():
        return False
    return Prime_Checker(Num, i + 2)

def Palindromic(text): #a recursive function that returns true if it runs through the whole string checking if it's palindromic
    
    if text == "":
        return True
    
    if text[0] == text[-1]:
        return (Palindromic(text[1:-1]))
    else:
        return False

def Not_A_Loop(Num, endNum): #runs through numbers using recursion and calls Palindromic and Prime checkers
    if Num == endNum+1:
        return
    
    if Palindromic(str(Num)):
        if Prime_Checker(Num, 3):
            print(Num)
    return Not_A_Loop(Num + 1, endNum)


Start = int(input("Enter the starting point N:\n"))
End = int(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
Not_A_Loop(Start, End)
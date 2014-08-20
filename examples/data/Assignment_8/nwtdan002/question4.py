'''A Program to print out a list of palindromic primes between 2 points
By Daniel Newton
04/05/14'''

import math
import sys
sys.setrecursionlimit (40000)   #Increases amount of recursion allowed


def palindromic(num):   #checks if the number is palindromic
    num=str(num)    #converts number to string for check to work
    if len(num)<2:
        return True
    if num[0]!=num[-1]:     #If characters at either end of the string are not equal, it is not palindromic
        return False
    return palindromic(num[1:-1])   #Removes first and last character (since these must be equal) and repeats check until the length of the string < 2.

def prime(num,limit):   #Function checks if number supplied is a prime
    if num==1:
        return False
    if num%limit==0:  #Number is divisible by some number below it therefore not prime
        return False
    elif limit>=int(math.sqrt(num)):    #Stops loop when number has been checked by all possible divisible numbers
        return True
    if num%limit!=0:
        return prime(num,limit+1)   #returns the function to check divisibility against the next number


def numchecks(num,num2):    #Does a prime and palindrome check for every number in range supplied
    if num==num2:   #recursion continued until limit of range met
        return
    if prime(num,limit)==True and palindromic(num)==True:
        print(num)  #If check is true, prints the number and goes onto the next number
        return numchecks(num+1,num2)
    else:   #Check is false, therefore no number printed, continue to next number
        return numchecks(num+1,num2)


limit=2 #limit=2 since all numbers are divisible by 1, so prime check must start by checking divisibility by 2.
num=eval(input("Enter the starting point N:\n"))
num2=eval(input("Enter the ending point M:\n"))
num2+=1 #To include the end point in the check
print("The palindromic primes are:")
numchecks(num,num2)
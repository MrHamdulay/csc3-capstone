"""This program uses recursive functions to find all palindromic primes
between two integers supplied as input (start and end points are included)
Masilela Mduduzi
7 may 2014"""
import sys
sys.setrecursionlimit (30000)

import math
#check if a number is a palindrome as a string
def palindrome(number):
    if len(number)<=1:
        return True
    elif number[0] != number[-1]:
        return False
    else:
        return palindrome(number[1:len(number)-1])
#checks if a number is a prime  
def prime(number,divisor):
    if number ==1:
        return False
    elif divisor<2:
        return True
    elif number % divisor==0:
        return False
    else:
        return prime(number,divisor-1)

#run through all th numbers between the start and the end and also call the other
#functions palindrome and prime to check each number and if it satisfy both the
#functions print it
def num(start,end):
    if start>end:
        return 
    else :
        if palindrome(str(start)) and prime(start,int(math.sqrt(start))):
            print(start)
        num(start+1,end)
        
if __name__=='__main__':
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    num(start,end)
        

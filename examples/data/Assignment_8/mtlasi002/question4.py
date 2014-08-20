#Asil Motala
#MTLASI002
#Assignment 8
#Question 4
#27 April 2014

import sys
sys.setrecursionlimit(30000)
from math import *

def palindrome(string):
    if string=="" or len(string)==1:                    #breaking condition - no letters left (even length string) or middle letter (odd length string)
        return True
    elif string[0]==string[-1]:                         #first letter equals last letter
        return palindrome(string[1:len(string)-1])      #check for second letter to second to last letter
    else:
        return False                                    #breaking condition for not a palindrome

beg=2
def prime(beg,number):
    if number==1:
        return False
    elif beg>sqrt(number):                             #breaking condition if it is a prime
        return True
    if number%beg!=0:                                   #check that it is a prime - not divisible by anything but 1 and itself
        return prime(beg+1,number)
    else:                                               #breaking condition for not a prime
        return False

def palindromic_prime(start,end):
    if start==end:                                      #breaking condition last number is being checked
        if palindrome(str(start)):                      #palindrome true
            if prime(beg,start):                        #prime true
                print(start)
                return True
            else:                                       #prime false
                return False
        else:                                           #palindrome false
            return False
    else:
        if palindrome(str(start)):                      #palindrome true
            if prime(beg,start):                        #prime true
                print(start)
                return palindromic_prime(start+1,end)   #continue to check through numbers
            else:                                       #prime false
                return palindromic_prime(start+1,end)   #continue to check through numbers
        else:                                           #palindrome false
            return palindromic_prime(start+1,end)       #continue to check through numbers

start=eval(input("Enter the starting point N:\n"))      #get input from user in integer type
end=eval(input("Enter the ending point M:\n"))          #get input from user in integer type
print("The palindromic primes are:")                    #print heading

def execute(start,end):
    if end-start>1000:                                  #if range is too big to process
        palindromic_prime(start,start+1000)             #break it down to a smaller part
        return execute(start+1000,end)                  #recursive for rest of range
    else:
        palindromic_prime(start,end)                    #if string is the right size

execute(start,end)                                      #invoke function
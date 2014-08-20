"""program to check palindromic primes using iteration
author: DIVAN JAGERS
DATE: 9 MAY 2014"""
import sys
sys.setrecursionlimit (30000)
from math import *
def palindrome(item):  #checks if the item is a palindrome
    if item == "":
        return True    #base case
    if len(item)<=1:
        return True
    else:
        if item[0] == item[len(item)-1]:
            return palindrome(item[1:len(item)-1])
        else :
            return False
def prime(start,end):   #checks prime numbers   
    if start==2:
        return True    #base case
    if start%end==0: #if it is divisible by the end point
        return False
    if (end>=sqrt(start)):
        return True
    else:
        return prime(start,end+1)
def palindromicP(start,end):   #combines the palindrome and prime function and checks if these intersect and then prints them
    if start>end:
        return True    #base case
    else:
        if palindrome(str(start)) and prime(start,2):
            print(start)
        start=int(start)
        palindromicP(start+1,end)
start =eval(input('Enter the starting point N:\n'))#prompts the user for the start and ending boundries
if start == 1 :    #makes the start 2 so as not complicate chekinn for primes
    start=2
end= eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
palindromicP(start,end)
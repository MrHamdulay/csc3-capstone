"""Program that uses recursive functions to find all palindromic primes between two integers supplied as input (start and end points are included)
Reece Gounden
7 May 2014"""

import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n")) #N
M = eval(input("Enter the ending point M:\n")) #M

if (N>1):
    num=N
else:
    num = 2
print("The palindromic primes are:")

def ref(num):
        
    if num > M: #terminate when the specified ending point is reached.
        return -1
    
    tcheck = chkpal(num)
    
    if  tcheck == True: #if current number is plaindrome sends to prime()
        d=2
        return prime(num, d)
    else: #checks if next number is palidrome is current is not
        return ref(num+1)
    
def chkpal(number):

    number = str(number) #Convert number to string.
       
    if number[0] == number[len(number)-1] and len(number) <= 3: #checks if palindrome for numbers with 3 or less digits
        return True
    
    elif number[0] == number[len(number)-1]: #checks if 1st = last number and if so checks the next inner numbers
        return chkpal(number[1:len(number)-1])
    
    else: #returns false if number is not a palindrome
        return False
    
def prime(num, div):
    
    if div <= num**(1/2): #program terminates if divisor > 1/2 of palindrome num
        if num%div == 0:
            return ref(num+1) #If pal number isnt prime checks for next palindrome
        else:
            return prime(num, div + 1) 
    else: #If number is palindrome and prime prints the number and searches for next palindromic num
        print(num)
        return ref(num+1)
    
ref(num)
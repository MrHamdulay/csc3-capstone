# a program that uses recursive functions to find all palindromic primes between two integers
# Retselisitsoe Monyake
# 9 May 2014


import sys
sys.setrecursionlimit (30000)

#Checking palindromes
def palindrome(string_no):
    if len(string_no) <= 1 :
        return True
    else :
        if string_no[0] == string_no[len(string_no)-1]: 
            return palindrome(string_no[1:len(string_no)-1])
        else:
            return False

# Checking for primes 
def prime_numbers (x, y):
    if (y>x**(1/2)):
        return True
    if x%y == 0 : 
        return False
    else:
        return prime_numbers(x,y+1)


x =eval(input("Enter the starting point N:\n"))
if x == 1 :
    x+=1
y= eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
    
 # Checking palindromic prime numbers   
def palindro_primes(x,y):
    if x> y:
        return
    else :
        if palindrome(str(x)) and prime_numbers(x,2):
            print(x)
        palindro_primes(x+1, y)


palindro_primes(x,y)
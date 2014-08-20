#uses recursive functions to find all palindromic primes between two points of input
#By Chloe Longmore
# 8 May 2014

#increase system recursion limit
import sys
sys.setrecursionlimit (30000)
base_no=2
    
def palin(number):
    string = str(number)
    last_pos=len(string)-1
    #base case if the string is empty
    if string=='':
        return True
    #compares first and last letters to see if the same
    elif string[:1] == string[last_pos:]:
        string=string[1:last_pos]
        #if the same, recurses program
        return palin(string)
    # if not the same, not a palindrome
    elif string[:1] != string[last_pos-1:]:
        return False

def prime(number,i):
    #2 is a prime
    if number == 2:
        return True
    #checks if number is divisible by 2, or less than two, therefore not a prime
    elif number < 2 or number%2 ==0:
        return False
    #checks if number divided by i gives a remainder of zero. i.e. divides in perfectly, indicating a non-prime
    elif number % i == 0:
        return False
    #
    else:
        if i == int(number**0.5)+1:
            return True
        #recursion step 
        else:
            return prime(number, i+1)

def palin_prime(n, m):
    #function that checks if numbers are palin and then if true, if they are prime
    #base case, checks if upper limit is equal to lower limit of input
    if n == m :
        #checks if a palindrome
        if palin(m):
            #checks if prime number
            if prime(m, base_no):
                print(m)
    #checks if the number ipnut is a palindrome
    elif palin(n):
        #checks if number is prime
        if prime(n, base_no):
            print(n)
            #recursion
            palin_prime(n+1, m)
        #recursion
        else:
            palin_prime(n+1, m)
    #recursion
    else:
        palin_prime(n+1, m)
        
#main function that calls the other functions and ask for input  
n = int(input("Enter the starting point N:\n"))
m = int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
palin_prime(n, m)
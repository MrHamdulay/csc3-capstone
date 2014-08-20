'''Palindromic primes between input values: Recursion
Adam Oosthuizen'''
import sys
sys.setrecursionlimit (30000)
i = 2#Global variable for checking prime numbers

def checkPrime(n):
    global i
    if i == n:#if the value entered is reached by the counter i
        return True
    elif (n % i == 0):#condition for falsehood
        return False
    else:#recursive step
        i += 1
        return checkPrime(n)

def checkPalindrome (s):
    s = str(s)
    '''returns a boolean value based on whether or not a string parameter is 
    a palindrome or not'''
    if s == "":
    #checks whether the string has been reduced to an empty string    
        return True
    
    elif s[0] != s[-1]:
    #compares the first character in a string to the last 
        
        return False
    else :
        #recurs the function if the characters thus far have supported a 
        #palindrome
        return checkPalindrome(s[1:-1])

def final(n,m):
    n = eval(n)
    m = eval(m)
    global i 
    i = 2
    if n == m :
        
        if checkPalindrome(n) == True and checkPrime(n) == True:
            print(n)
    elif checkPalindrome(n) == True and checkPrime(n) == True:
        print(n)
        return final(str(n+1),str(m))
    else:
        return final(str(n+1),str(m))
    
            
        
    
n = input("Enter the starting point N:\n")
m = input("Enter the ending point M:\n")
print("The palindromic primes are:")
final(n,m)


            
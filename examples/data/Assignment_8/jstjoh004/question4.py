# Recursion
# find all palindromic primes 
# Hendrik Joosten
# JSJOH004
# 04 May 2014


# import various classes to user in the program
import math
import sys
# set the recursion limit to a higher value
# PS this strangely does not change the stack size
sys.setrecursionlimit (30000)


# this method checks ifa number is a prime number
def isPrime(x,y):
    # check if == 2 since it is the only even prime number, also  the smallest
    # base case
    if x==2:
        return True
    # do this if the input is bugger that 2
    elif x>2:
        # devide the number you want to check by all y  2 < y < (sqrtnumber you want to check)
        if y == 1:
            return True
        # if the mod is 0 you know it has a factor and thus it is not a prime
        else:
            if (x % y == 0):
                return False
            else:
                #decreases the y value
                return isPrime(x,y-1)
    else:
        return False  
    
    # this method is very simalar to the palindrome checking mwthod in question 1
def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[len(s)-1]:
        return isPalindrome(s[1:len(s)-1])
    else:
        return False
    
# this is the method that combines methods prev coded in this program
def isPalindromicPrime(n,m):
    # base c ase if starting point is ending point + 1
    # end recursion
    if n >= m+1:
        return 1
    #checks if number is a prime with function isPrime()
    # send over the number being checked and the sqrt of that number as parameters
    elif isPrime(n,int(math.sqrt(n))):
        #if it IS a prime check if it is a palindrome
        if isPalindrome(str(n)):
            # if both conditions are met print the number
            print(n)
            # recall the function and iterate the sarting point cause that is the number the test
            # are being done on!
            return isPalindromicPrime(n+1,m)
        else:
            return isPalindromicPrime(n+1,m)
    else:
        return isPalindromicPrime(n+1,m)


n = input("Enter the starting point N:\n")
n = eval(n) 
m = input("Enter the ending point M:\n")
m = eval(m)
print("The palindromic primes are:")


isPalindromicPrime(n,m)
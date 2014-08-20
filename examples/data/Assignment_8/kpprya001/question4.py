import sys

import math

sys.setrecursionlimit (30000)
#get in
startN = eval(input('Enter the starting point N:\n'))
startM = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:\n',end="")
isPrime = True
counter = 2
def find_prime(startN,startM,isPrime,counter):
    if(startN != 1):
        if(startN <= startM):
            if(find_palindrome(str(startN),str(startN))):
                if(counter<startN):
                    if(isPrime):
                        if(startN % counter ==0):
                            isPrime = False
                            return find_prime(startN,startM,isPrime,counter)
                        else:
                            counter+=1
                            return find_prime(startN,startM,isPrime,counter)
                    else:
                        return find_prime(startN+1,startM,True,2)
                else:
                    print(startN)
                    return find_prime(startN+1,startM,True,2)
            else:
                
                return(find_prime(startN+1,startM,True,2))
    else:
        return(find_prime(startN+1,startM,True,2))
    
 
def find_palindrome(string1,string2):
    #if the string is not blank, then carry on
    if (string1!=""):
        if(string1[0:1]==string2[-1:]):
            isPalindrome = True
            return(find_palindrome(string1[1:],string2[:len(string2)-1]))
        else:
            isPalindrome = False
            return isPalindrome
    else:
        isPalindrome = True
        return isPalindrome
    
    
find_prime(startN,startM,isPrime,counter)
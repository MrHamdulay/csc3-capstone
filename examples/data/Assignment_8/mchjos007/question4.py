import sys
sys.setrecursionlimit (30000)

i = 2
def is_prime_number(n, i):
    if i == n:
        return True
    elif (n % i == 0):
        return False
    elif(n > i):
        i = i + 1
        return is_prime_number(n,i)
    
def isItAPalindrome(theStringInQuestion):
    if len(theStringInQuestion) == 1 or len(theStringInQuestion) == 0:
        return True
    if theStringInQuestion[0] == theStringInQuestion[-1]:
        if isItAPalindrome(theStringInQuestion[1:-1]):
            return True
    else:
        return False    
    
def printTheThings(startpoint,endpoint):
    if startpoint == endpoint:
        if isItAPalindrome(str(startpoint)):
            if is_prime_number(startpoint,2):
                print(str(startpoint))
    else:
        if isItAPalindrome(str(startpoint)):
            if is_prime_number(startpoint,2):
                print(str(startpoint)) 
        return printTheThings(startpoint+1,endpoint)
            
    

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
printTheThings(N,M)

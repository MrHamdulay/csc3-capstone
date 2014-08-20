#9 May 2014
#Program to find palindromic primes between two numbers
#LYLJON002

import sys
sys.setrecursionlimit(30000)   

def prime(divisor, k):  #check to see if number is prime
    if k < 2:
        return False        # 1 and lower are not prime, returns false
    if k == 2:
        return True             #2 is only even prime number
    if k%divisor == 0:  
        return False                #not a prime number
    elif (k)**(1/2) <= divisor:  
        return True                 #more efficient to go to the root of k
    if k%divisor != 0:
        return prime(divisor + 1, k)    #recursive statement



def pal(text):                              #function to test
    text=str(text)
    if len(text) <2 :
        return True                    #if one character or empty then its a palindrome
    last = text[-1]
    first = text[0]
    if first == last:                   #check first and last letters
        return pal(text[1:-1])      #return string with first and last letters removed, repeat function
    return False


def test(l,z):    
    if z == l: #no numbers to move through
        return
    if prime(divisor, l) == True:
        if pal(l) == True:
            print(l)  
            j = l + 1
            return test(j, z)   
    j = l + 1
    return test(j, z)


divisor = 2

l =eval(input("Enter the starting point N:\n"))
z =eval(input("Enter the ending point M:\n"))

z = z + 1 

print("The palindromic primes are:")
test(l, z)
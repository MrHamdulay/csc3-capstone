import math   #used in sqrt function 
import sys
sys.setrecursionlimit (30000)   #as specified in instructions this is to increase the amount of recursion that Python will allow
def prime(num,div): 
    if num==1:
            return False    #base case in boolian 1st variable
        
    if num == 0:
        return False        #another base case 1st variable
     
    
    if div>=2 and div<=math.sqrt(num):   #the 2nd variable needs to be between 2 and the sqrt of the number so the program to save memory and avoid it being aborted
        if num%div == 0:    # if the number has a divisor then it is not a prime and you stop thre and not include a recursive step
            return False
        else:
            return prime(num,div +1)    # if the number variable is not a multiple of the specific divisor, continue searching but using a recursive step until the sqrt of the number is equal to div
    else:
        return True           #if all the divs were used then say yes it is a prime number and store it
def Prime(num):                      #we use this function to use 1 variable so that it can be used in the check_prime_palindrome function 
    return prime(num,2)         #we are calling the 1st prime function but div starts with 2 all the time this is all easier as 1 variable can now be used

def reverse(num):         #this function reverses the number inputed within the range
    num =str(num)          #making the number into the string so that we can use the function reverse to reverse the word  
    if len(num) <=1:        #this is the base case whre you can just return the number itself
        return num                   
    else: 
        return reverse(num[1:]) + num[0]    #this is the recursive step inclusive of each incrimented string to reverse the string
    

def palindrome(num):
    return str(num) == reverse(num)          #this function is used in the  check_prime_palindrome function with satisfying condition that it is a palindrome 


def check_prime_palindrome(N,M):        #this function takes in variables N and M specifically    
    
    #palindrome(num)
   
    
    if N>M:                                      #base case boolian dont do anything if N exceeds M
        return 
    if palindrome(N) == True:                           #where this functions are satisfied display the N and do the recursive step
        if Prime(N)==True:

            print(N)
            return check_prime_palindrome(N+1,M)
        else:                                               #here whre the two function conditions are not satisfied just look for the next value of N implying the recursive step
            return check_prime_palindrome(N+1,M)
    else:
        return check_prime_palindrome(N+1,M)                    #we want to make sure if the N does not even go into the conditon statement the recursion still continues
                
    
    
N =int(input('Enter the starting point N:\n'))                   #displaying for out put at the bottom of the functions this used in more understandable work for the next person to understand the code
M = int(input('Enter the ending point M:\n'))
print("The palindromic primes are:")

check_prime_palindrome(N,M)                                 #calling the function
    
    

    
    
    

    
    
    

    
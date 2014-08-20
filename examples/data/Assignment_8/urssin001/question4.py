#Write  a program that uses recursive functions to find all palindromic primes 
#between two integers supplied as input (start and end points are included).
#Sinead Urisohn
#6 May 2014
#to increase the amount of recursion that Python will allow:
import sys
sys.setrecursionlimit (30000)
#get starting number
start=eval(input("Enter the starting point N:\n"))
#get ending number
end=eval(input("Enter the ending point M:\n"))

def numbers(n,m):
    '''recursive function to generate all the numbers from starting to end number
    that receives start and end numbers as parameters'''    
    #current number is the first parameter
    current_num=n
    
    #base case - if current number is equal to ending number
    if current_num==m:
        #send last number into palindrome check function
        palindrome(m)
       
    else:
        #else send in between number into palindrome check function
        palindrome(current_num)
        #return recursive function to generate next sequential number in range 
        #from n including m
        return numbers(n+1,m)
def num_reverse(a):
    '''reverses number using % and integer division'''
    #if only 1 unit left i.e. number from 1-9
    if a<10:
        #return last number as string
        return str(a)
        
    
    else:
        #otherwise add last digit as string and recurse through the rest of number
        #excluding last digit
        return str(a%10) +num_reverse(a//10)
def palindrome(num):
    ''' checks if number palidrome'''
    #if number equal to itself reversed
    if str(num)==num_reverse(num):
        #send half of number and number into prime check function
        prime(num//2,num)
def prime(x_mul,x):
    '''recursive function that checks if a number x is a prime number by
    checking its divisibility with numbers half of its amount until 1 reached'''
    #base case
    #if number is 1 return false
    if x==1:
        return 0
    #if the multiple of x reaches 1
    #then no factors found
    if x_mul==1:
        #send x into display function
        display(x)
        #return true that x prime number
        return 1
    else:
        #if number has factors
        if x%x_mul==0:
            #return false
            return 0
        #else if not factor, check next smaller number for multiple of x
        else:
            #recursive step where possible x multiples decreased by one
            return prime(x_mul-1,x)
#print heading
print("The palindromic primes are:")
def display(x):
    '''displays prime number palidromes'''
    print(x)
    
#send start and end numbers to generate numbers to be checked
numbers(start,end) 
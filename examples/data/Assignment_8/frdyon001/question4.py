"""YONELA FORD
FRDYON001
04 MAY 2014"""

import sys
sys.setrecursionlimit (30000)
#get starring and ending values from user
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

#use palidrome check from question1
import question1
import math


#check if the number is prime by setting start to and if it is divisible by this then it fails check, otherwise keep incrementing start to check for all the factors of the number up until the squareroot of the number itself
def check_prime(start,prime):
    #make sure that the number is greater than 2 first
    if prime <2:
        return False    
    elif start>math.sqrt(prime):
        return True
    elif prime%start!=0:
       return check_prime(start+1,prime)
    else:
        return False
#combine both the checking for a palindrome programme and the checking for a prime number programme for the range in designated values    
def other(start,end):
    #ensure that we start at the lower end of the range 
    if start<=end:
        #check if number is a palindrome
        palin=question1.palin(str(start),0)=="Palindrome!"
        if  palin:
            #if it is a palindrome then check if it is a prime number
            if check_prime(2,start)==True:
                print(start)
        #continue two_step process recursively
        return str(other(start+1,end))
    else:
        return " "
                

print(other(start,end))
        

            
"""a program that uses recursive functions to find all palindromic primes between two integers supplied as input.
fadzai mupfunya
08 may 2014"""
import math
import sys
sys.setrecursionlimit (30000)

num=eval(input("Enter the starting point N:" '\n'))
M=eval(input("Enter the ending point M:" '\n'))
print("The palindromic primes are:")

"""function that turns the input to a palindrome"""
index=0    #index has to start at 0 for function to work 
def pali(num, index): 
        num=str(num)
        if int(len(num)//2) == index:
                return True 
        if num[index] != num[len(num)-1-index]: 
                return False
        else:
                return pali(num, index+1) 
        
"""function that checks to see if it is a prime number"""
div=2        
def prime(num, div):
        if num==1:
                return False 
        elif num==0:
                return False             
        elif div >= 2 and div <= math.sqrt(num): 
                if num%div == 0:
                        return False 
                else:
                        return prime(num,div+1)
        else:
                return True

pali_prime_list=[] #to store all the palindromic primes

def pali_prime(num):
        if num<=M: #to make sure the number lies between the starting point and ending point
                if pali(num, index)==True and prime(num, div)==True:    #to make sure it only collects the prime numbers and palindromic numbers
                        pali_prime_list.append(num)
                        return pali_prime(num+1)
                else:
                        return pali_prime(num+1)
        else:
                return pali_prime_list
l=pali_prime(num)
def print_nums (l):
        if len(l) > 0:
                # to print out first item
                print (l[0])
                # to print out the rest of list
                print_nums (l[1:])
print_nums(l)

        
                
                
        
        
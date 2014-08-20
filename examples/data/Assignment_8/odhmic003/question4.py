"""Michael Odhiambo
ODHMIC003
Assignment 8_Question 4
Program to search for palindomic prime numbers within a given interval"""
import sys
sys.setrecursionlimit (30000)
"""Prompt user for input"""
n= eval(input("Enter the starting point N:\n"))
m= eval(input("Enter the ending point M:\n"))

ans=[]
def Pal_prime(n,m):
    a= n*1
    b= m*1
    if n<=m:
        global array
        array=[]        
        if a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0 and a%11!=0 and a%13!=0 and a%17!=0 and a%19!=0 and a!=1:# Check to see whether number is prime
            """Function to recursively check if number is a palindrome and append palindromic primes to an array""" 
            def makelist(n):
                
                N= str(n)
                if len(N)>=1:
                    x= N[0]
                    array.append(x)
                    makelist(N[1:])
                    
            makelist(n)
            array1= array*1
            array1.reverse()  
            if array==array1: 
                ans.append(n)
                Pal_prime(n+1,m)
            else:
                Pal_prime(n+1,m)
        elif n==2 or n==3 or n==5 or n==7 or n==11:
            ans.append(n)
            Pal_prime(n+1,m)
        else:
            Pal_prime(n+1,m)
    else:
        return 0
Pal_prime(n,m)
print("The palindromic primes are:")
"""Recursive function to print each palindromic prime from array"""
def unpack(ans):
    if len(ans)>=1:
        x= ans[0]
        print(x)
        unpack(ans[1:])
unpack(ans)



"""Question 4- Assignment 8
Duncan Saffy
May 6 2014"""
import sys
sys.setrecursionlimit (30000)

def pal(x):
    if x[0]==x or x[0:2]==x:
        return 1
    
    elif x[0]==x[-1]:
        return pal(x[1:(len(x)-1)])
    
    else:
        return 0

def prime(x,y,z):
    if x%z==0:
        return (x+1,y,z) 
    else:
        return (x,y,z+1)
    

z=2
x= input("Enter the starting point N:\n")
y= input("Enter the ending point M:\n")
print("The palindromic primes are:")
if pal(prime(x,y,z))==0:
    print(prime(x,y,z))
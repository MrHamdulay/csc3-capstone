"""palindromic primes
ringo shima
9/5/14"""
import math
import sys
import question1
sys.setrecursionlimit (30000)

def primepal(n,m,x):
    #base case
    if n==m:
        x = str(n)
        y = question1.pal(x) #run q1 module
        if y == "Palindrome!": 
            return x
        else:
            return x
        
    elif n<m:
        
        x = str(n)
        y = question1.pal(x)
        n+= 1
        
        if y == "Palindrome!": #check if palindrome or not
            print (x) 
            return primepal(n,m,x)
        else:
            return primepal(n,m,x)
    print()
       
     
def main():
    n=eval(input("Enter the starting point N:\n"))
    m=eval(input("Enter the ending point M:\n"))
    
    print("The palindromic primes are:")
    primepal(n,m,"")
main()

#haven't worked out primes yet 

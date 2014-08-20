# a program to calculate palindromic primes
# mashau zwivhuya
# 6 may 2014
#increasing recursion
import sys
sys.setrecursionlimit (30000)
#getting inputs
start=eval(input("Enter the starting point N:\n"))
end=input("Enter the ending point M:\n")

print("The palindromic primes are:")
#calculating palindromes
def isPal(s):
        s=str(s)
        if (len(s) < 2):  
        #is true
                return True

        if (s[0] != s[-1]):
                return False  
        return isPal(s[1:-1]) 
#calculating primes
def prime(x,start):
        
        if int(start)==1:
                return False
        if int(start)==2:
                return True
        if x == int(start):
                return True
        if int(start)%x==0:
                return False
        else:
                return prime(x+1,start)
   

# joining the two functions and printing palindrome primes
        
def pal_prime(start,end):
        if int(start) == int(end):
                return 0
        
        #if isPal(start):
                #print(start,"pall")
        if prime(2,start) and isPal(start) :
                print(start)
        return pal_prime(int(start)+1,end)
pal_prime(start,end)


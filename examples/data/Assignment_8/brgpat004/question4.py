'''Q4 of Assignment 8: Finding all palindromic primes between 2 integers
Patrick Boroughs
4 May 2014'''

#imports
import sys
import math
import question1

#increase amount of recursion Python will allow
sys.setrecursionlimit(30000)

def palinprime(n,m, fact):
	
	#run until up to end point M
	if n<=m:
		#test if n is a palindrome
		if not question1.palindrome(str(n)):
			palinprime(n+1,m,round(math.sqrt(n+1)))
			
		#don't test for primality if num is less than 2
		elif n < 2:
			palinprime(n+1,m,round(math.sqrt(n+1)))
			
		#exception prime when n is 2 (sqare root will round to 1)		
		elif n==2:
			print (n)
			palinprime(n+1,m,round(math.sqrt(n+1)))
				
		#factor found, not prime
		elif n % fact == 0:
			palinprime(n+1,m,round(math.sqrt(n+1)))
			
		#factor not found, test one number lower
		elif n % fact != 0 and fact != 2:
			palinprime(n,m, fact - 1)
			
		#no factors found up till 2. Prime found.
		elif n % fact != 0 and fact == 2:
			print (n)
			palinprime(n+1,m,round(math.sqrt(n+1)))
				
#input start and end				
n1 = eval(input("Enter the starting point N:\n"))
m1 = eval(input("Enter the ending point M:\n"))

#test factors up to sqare root of n
fact = round(math.sqrt(n1))

#output
print("The palindromic primes are:")
palinprime(n1,m1, fact)
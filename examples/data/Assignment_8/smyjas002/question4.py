#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 6
#question 3

import math
#to allow python to create a large enough stack
import sys
sys.setrecursionlimit (30000)

def isPrime(number, testFactor):
	# first base case, to test if the number is 1 or 2 whitch are by definition not prime
	if number < 2:
		return False
	# second base case, if the testFactor is bigger than half af the number it cannot be a foctor of the number.
	elif testFactor > math.sqrt(number):
		return True
	# third base case, for when the number has a factor and is thus prime
	elif number%testFactor == 0:
		return False
	# recursive step, incremets the testFactor until a base case is reached
	else:
		return isPrime(number, testFactor + 1)
	
	
def isPalindrome( testStr ):
    # base case, used if gone through whole string withought issue. 
    if len (testStr) < 1:
        return True
    # first recursive step, checks if the first and last letter is the same.
    elif testStr[0] == testStr[-1]:
        return isPalindrome(testStr[1:len(testStr) - 1])
    # second recursive step, if it does not match it is not a palindrome.
    else:
        return False
                
def rangTester( startNum, endNum ):
	# base case, checks if the startNum is still in range
	if startNum > endNum:
		return
	# second base case, prints out the sollution if the criteria is met
	elif isPrime(startNum, 2):
		if isPalindrome( str(startNum) ):
			print(startNum)
	# inductive step, runs through the numers in the given range
	rangTester( startNum + 1, endNum )  

def main():
	n = eval(input("Enter the starting point N:\n"))
	m = eval(input("Enter the ending point M:\n"))
	print("The palindromic primes are:")
	rangTester( n, m )
	
main()



"""
Enter the starting point N:
200
Enter the ending point M:
800
The palindromic primes are:
313
353
373
383
727
757
787
797
"""

#WHTBAS001
#ASSIGNMENT 3
#QUESTION 4
#25-03-2014

import math

N = int(input("Enter the starting point N:\n"))
M = int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def prime(x):
	root = math.ceil(math.sqrt(x))
	for i in range(2, root+1):
		if x%i == 0:
			return False
	return True

def palendrome(x):
	strx= str(x)
	if strx == strx[::-1]: 
		return True
	else:
		return False

for i in range(N+1, M):
	if i%2 != 0 and i !=2 :
		if prime(i) == True:
			if palendrome(i) == True:
				print(i)
	elif i == 2:
		print(i)

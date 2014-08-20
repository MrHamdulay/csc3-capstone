#Grant Meeser
#MSRGRA002
#08/05/2014

import sys
sys.setrecursionlimit (50000)

def pall(s):
	if round(len(s)/2) != 0:
		if s[0] == s[len(s)-1] and pall(s[1:len(s)-1]):
			return True
		else:
			return False
	else:
		return True

def prime(n,d):
	if d>2:
		if n%(d-1) >0 and prime(n,d-1):
			return True
		else:
			return False
	else: return True

def printPallPrimes(start,end):
	if start<=end:
		if pall(str(start)):
			if prime(start,start) and start!=1:
				print(str(start))
		printPallPrimes(start+1,end)



start = int(input('Enter the starting point N:\n'))
end = int(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
printPallPrimes(start,end)


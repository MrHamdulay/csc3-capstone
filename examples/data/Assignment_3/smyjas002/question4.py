import math

def main():
	x = eval(input("Enter the starting point N:\n")) + 1
	y = eval(input("Enter the ending point M:\n")) - 1
	print("The palindromic primes are:")
	for i in range(x, y+1):
		if primeTest(i):
			if palindrome(i):
				print(i)


def primeTest(a):
	if a==1:
		return False
	for i in range(2, (a//2)+1):
		if (a%i) == 0:
			return False
	return True

def palindrome(a):
	digitList =list(str(a))
	digitLength = len(digitList)
	for i in range(0, digitLength//2):
		#print("left digit" + str(i))
		#print("left digit" + str(digitLength - i - 1))
		if digitList[i] != digitList[digitLength - i - 1]:
			return False
	return True
			#print("digit ok" + digitList[i])
		#else:
			#print("digit BAD" + digitList[i])

main()
#for i in range(20):
#	print(palindrome(eval(input("enter a test number:\n"))))


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

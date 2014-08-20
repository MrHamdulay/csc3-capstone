# A program that prints the palindromic primes
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011

# Prompt the user for input
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))


# Check if the number is palindrome
def palindrome(number):
    return str(number) == str(number)[::-1]
	
# check whether the number is a prime number
def Prime(n):
	divisor = 2
	while divisor <= n / 2:
		if n % divisor == 0:
			# If true, number is not prime
			return False # number is not a prime
		divisor += 1

	return True # number is prime

def printPalindromes(x,y):
	# Repeatedly find prime numbers
	while x < y and x != 1:
		# Print palindrome and increase the count
		if Prime(x):
			if palindrome(x):
				print(x)

		# Check if the next number is prime
		x += 1

def main():
	print("The palindromic primes are:")
	printPalindromes(N,M)

main()		# Call the main function
#Program to check for palindromic primes between two numbers
#Matthew Bandama
#BNDTAT003
#08-May-2014

import question1,sys
sys.setrecursionlimit (300000000)



def prime(num,checker):
	
	if checker == 1:
		return(True)
	if checker < 0:
		return(False)
		
	else:
		
		check = num%checker
		
		if check == 0:
			checker = -1
		return(prime(num,checker-1))




def pal_prime(n,m):
	
	if n == m+1:
		return
	
	else:
		a = round(n**0.5)
		
		if prime(n,a) == True and question1.palindrome(str(n)) == True and n != 1:
		
			print(n)
			return(pal_prime(n+1,m))
		else:
			return(pal_prime(n+1,m))

def main():
	print('Enter the starting point N:')
	start = eval(input())
	print('Enter the ending point M:')
	end = eval(input())
	print('The palindromic primes are:')
	pal_prime(start,end)



if __name__=='__main__':
	main()


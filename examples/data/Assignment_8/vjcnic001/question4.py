#Program checks for palindromic primes
#Nicol Vojacek

import sys
sys.setrecursionlimit (30000)

a = eval(input("Enter the starting point N:\n"))
b = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")


def prime(p,k):
    if p == k: 
        return True
    if (p%k == 0) or (p < k): #If not a prime, return False
        return False
    return prime(p,k+1) #increase counter to check if numbers within number make it prime

def pal_prime(p):
	if p == "":
		return ""  
	if str(p)[0] == str(p)[-1]: 
		return prime(p,2)
	else:
		return False

def num_range(a,b):
    if a > b: #If starting number more than ending number we want to exit 
        return ""
    else:
        if pal_prime(a): #Print the palindromic prime if it exists 
            print(a)
        num_range(a+1,b) #Increase range, getting closer to ending point

num_range(a,b)

	

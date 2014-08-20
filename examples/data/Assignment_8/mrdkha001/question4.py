"""Program that gets palindromic integers
Khanyisile Morudu
08 May 2014"""

#importing
import sys, math
sys.setrecursionlimit (30000)


# Some examples of palindromic primes are: 11, 191, 313

#variables
i = 2 #will be made global in prime function
list_check = "" #will be made global in palindrome function

#input 
num_start = input("Enter the starting point N:\n")
num_end = input("Enter the ending point M:\n")

#recursive prime function, it returns none if number is a prime
def prime_check(n):
    #i variable
    global i
    #checking for prime
    if (n ==1):
        return False
    elif (n == 2):
        return True
    elif (n % i == 0) and (i <= math.ceil(n**0.5)):
        return False
    elif (n % i ==0) and (i == n):
        return True
    elif (n % i != 0) and (i <= math.ceil(n**0.5)):
        i = i + 1
        return prime_check(n)
    elif (n % i != 0) and (i >= math.ceil(n**0.5)):
        return True    
    elif (n > i):
        i = i + 1
        return prime_check(n)

#recursive palindrom function
def pal_check(n):
    if len(n) < 1:
        return True
    elif n[0] != n[-1]:

        return False
    elif n[0] == n[-1]:
        return pal_check(n[1:len(n) - 1])

#recursive palindrome function
def prime_palindrome(N, M):
    #print(N + "!")
    a = 0
    global list_check
    global i
    i = 2
    #This is for when N = M 
    if (N == M) and (pal_check(N) == False) and (prime_check(int(N)) == True):
        return list_check
    elif (N == M) and (pal_check(N) == False) and (prime_check(int(N)) == False):
        return list_check
    # Only gets into list of all conditions are met
    elif (N == M) and (pal_check(N) == True) and (prime_check(int(N)) == True):
        return list_check + N + "\n"
    elif (pal_check(N) == False) and (prime_check(int(N)) == True):
        return list_check + prime_palindrome(str(int(N)+1), M)
    elif (pal_check(N) == True) and (prime_check(int(N)) == False):
        return list_check + prime_palindrome(str(int(N)+1), M)
    #valid thus should be in list
    elif (pal_check(N) == True) and (prime_check(int(N)) == True):
        return list_check + N + "\n"  + prime_palindrome(str(int(N)+1), M)
    elif (pal_check(N) == False) and (prime_check(int(N)) == False):
        return list_check + prime_palindrome(str(int(N)+1), M)
    elif (pal_check(N) == False) and (prime_check(int(N)) == True):
        return list_check + prime_palindrome(str(int(N)+1), M)

#output
print("The palindromic primes are:")
print(prime_palindrome(num_start, num_end))

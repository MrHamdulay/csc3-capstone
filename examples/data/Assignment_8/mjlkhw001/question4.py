# Palindromic Primes
# Khwezi Majola
# MJLKHW001
# 04 May 2014

import question1 #Import for use of palindrome checker
import math #Import for limiting the checking of prime numbers
import sys #Import to increase recursion limit
sys.setrecursionlimit (30000) #Increase recursion limit

def palin_primes(n, m):
    global i #Makes i a global variable
    i = 2 #Resets i to 2
    count = 0 #Counter of factors
    if n == m: #End case for recursion
        if prime(n, i, count) == 0: #Checks if the factor count is 0
            if question1.palin(str(n)): #Checks if it is a palindrome
                if n != 1 and n != 0: #Excludes 0 and 1 from printing
                    print(n) #Prints
                return #End the recursion
            return #Above
        return #Above
    else:
        if prime(n, i, count) == 0: #Same as above
            if question1.palin(str(n)): #Same as above
                if n != 1 and n != 0: #Same as above
                    print(n) #Same as above
                return palin_primes(n+1, m) #Recursion occurs using n + 1
            else: return palin_primes(n+1, m) #Above
        else: return palin_primes(n+1, m) #Above

def prime(j, i, count): #Checks if a number is prime. Takes in "j" - the number to check, "i" - the factor & "count" - the number of factor which produce whole number
    if i <= math.ceil(j/2): #Stops the loop if "i" exceeds halfway of "j"
        if j%i == 0: #Checks if "i" is a factor
            count += 1 #Increases thus increase the factors
            i += 1 #Increases thus getting a new factor
            return prime(j, i, count) #Recursion occurs using the changed "count", "i"
        else:
            i += 1 #Same as above
            return prime(j, i, count) #Recursion occurs using the changed "i"
    else: 
        return count #Returns count. Count is zero when prime as 1 isn't included in division nor is "j"/the number being checked
    
def main(): #Input output function
    n = eval(input('Enter the starting point N:\n'))
    m = eval(input('Enter the ending point M:\n'))
    if n != '' and m != '': #Ensures actual values are inputted
        print('The palindromic primes are:')
        palin_primes(n, m)

main()
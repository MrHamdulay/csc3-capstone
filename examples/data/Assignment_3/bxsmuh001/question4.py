#Assignment 3, Question 4
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 27/03/2014; Updated: 28/03/2014

#This program is used to find all the palindromic primes between 2 values.

#Defining the function palimPrime() to find the palindrome primes.
def palimPrime():
    #Pre-condition: Input first and last numbers.
    #Post-condition: Output all the computed palindrome primes.
    n = eval(input("Enter the starting point N:\n"))
    m = eval(input("Enter the ending point M:\n"))
    n += 1
    print("The palindromic primes are:")
    for i in range(n,m):
        isPrime = True
        if(str(i) == str(i)[::-1]):
            if(i == 2):
                print(i)
            if(i>2):                
                for a in range(2,i):                
                    if(i%a==0):
                        isPrime = False
                        break
                if isPrime:
                    print(i)

palimPrime()
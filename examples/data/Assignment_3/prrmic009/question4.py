# Program to give all of the palindromic primes between two input values
# Mick Perring
# 28 March 2014

def palin ():                                            # Function to check if palindrome
    x = eval(input("Enter the starting point N:""\n"))   # Lets user input a starting point
    y = eval(input("Enter the ending point M:""\n"))     # Lets user input a ending point
    print ("The palindromic primes are:")
    if x < 1:
        print (1)          # prints 1 as a palindromic prime if it is in the range (not printed in function)
    for k in range (x+1, y):            # Checks for palindrome
        if k>=2:
            palin = int(str(k)[::-1])
            if palin == k:              # If palindrome, runs prime function
                prime (k)

def prime (z):                          # Function to check if prime (runs only if palindrome)
    prime = True
    for i in range (2, round(z**0.5)+1):  # Checks if NOT prime
        if z%i==0 and z!=i:
            prime = False
    if prime:  
        print (z)                       # If prime (and palindrome), prints number 
    
        
palin ()
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

#function tests whether input is prime. Prime returns True.
def is_prime(x): 
    if x < 2: # by definition, everything below 2 is NOT prime, including 1.
        return False
    elif x == 2: # 2 is prime
        return True
    else:
        for i in range(2, x):
# if any number between 2 and the number itself is a whole divisor of x, it's not prime  
            if x % i == 0:
                return False
        else:
            return True
                
print ("The palindromic primes are:")

for number in range(N+1, M): # from N to M excluding N and M
    number = str(number)
  # if number is palindromic and number returns True when inputted into above function:
    if number[::] == number[::-1] and is_prime(int(number)) == True:
        print (number)        
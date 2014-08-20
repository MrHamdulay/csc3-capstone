def isprime(n):
    '''check if integer n is a prime'''
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    for x in range(3, n, 2):
        if n % x == 0:
            return False
    return True



start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(start+1, end):
    st1 = str(i)
    if (st1 == st1[::-1]): #is a palindrome
        if (isprime(i) == True):
            print(i)
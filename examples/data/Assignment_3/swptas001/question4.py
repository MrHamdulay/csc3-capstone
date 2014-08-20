# Tashiv Sewpersad
# CSC1015F
# Assignment 3 - Question 2

# declarations
def isPrime(iNum):
    if iNum > 1:
        sResult = True
        for i in range(2,iNum//2+1):
            if iNum%i == 0:
                sResult = False
        return sResult
    else:
        return False
        
# live code
iLower = eval(input("Enter the starting point N:\n"))
iUpper = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
if iLower >= 0:
    for i in range(iLower+1,iUpper):
        sNum = str(i)
        if (sNum == sNum[::-1]) and (isPrime(i)==True):
            print(i)
            
else:
    print("The lower bound must be not be negative!")

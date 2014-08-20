N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print ("The palindromic primes are:")
for x in range (N+1, M):
    isPalindromicPrime = True
    tempString = str(x)
    for y in range (0, len(tempString)//2+1):
        if (tempString[y] != tempString[len(tempString)-1-y]):
            isPalindromicPrime = False
    if isPalindromicPrime:
        for y in range (2, x):
            if (x%y == 0):
                isPalindromicPrime = False
    if isPalindromicPrime:
        print (x)
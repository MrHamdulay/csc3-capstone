def hasFactors(n):
    factors = 0
    for j in range(1,n+1):
        if n%j == 0:
            factors +=1
        if factors > 2:
            return False
    return True
    
       
def isPalindrome(n):
    original = n
    s = 0
    while n > 0:
        r = n%10
        n = n//10
        s = s*10 + r
    if s == original :
        return True
    else :
        return False
    
minV = eval(input("Enter the starting point N:\n"))
maxV = eval(input("Enter the ending point M:\n"))
    
print("The palindromic primes are:")
for i in range((minV+1), (maxV)):
    if isPalindrome(i) and hasFactors(i):
        print(i)
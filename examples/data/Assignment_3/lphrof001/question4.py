import math
def is_prime(roo):
    if roo==1:
        return False 
    if roo % 2 == 0 and roo > 2: 
        return False
    for p in range(3, int(math.sqrt(roo)) + 1, 2):
        if roo % p == 0:
            return False
    return True

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    j=str(i)
    Rev_Pali=j[::-1]
    Rev_Pali2=i
    if j==Rev_Pali:
        if is_prime(i)==True:
            print(j)
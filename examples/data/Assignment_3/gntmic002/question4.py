#assignment 3.4
import math

def Pala(s):
    if s==s[::-1]:
        return True
    return False


def Prime(n):
    if n%2==0 and n>2:
        return False
    for k in range(3, int(math.sqrt(n)+1)+1,2):
        if n%k==0:
            return False
        
    return True

s = eval(input("Enter the starting point N:\n"))
e = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for k in range(s+1, e):
    if Pala(str(k)) == True and Prime(k) == True:
        print(k)
        
    
# Assignment 3 question 4
# Amy Brodie
# 27/03/2014

import math

def prime(x):
    if x<2:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    else:
        for pr in range(3,round(math.sqrt(x))+1,2):
            if x%pr==0:
                return False
        return True

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(start+1,end):
    n = i
    if prime(i):
        p = ""
        while n:
            p += str(n%10)
            n = n//10
        if p == str(i):
            print(i)
    
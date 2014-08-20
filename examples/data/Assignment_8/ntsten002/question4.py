import sys
import math
sys.setrecursionlimit(300000)

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
    
def prime(a, b):
    if b < 2:
        return False
    elif a>math.sqrt(b):
        return True
    elif b%a != 0:
        return prime(a+1, b)
    else:
        return False
    
def reverse(string):
    if string == "":
        return string
    else:
        new_string = reverse(string[1:])+ string[0]
        return new_string

print("The palindromic primes are:")    

def increments(m, n):
    if m == n:
        return m
    else:
        if reverse(str(m)) == str(m):
            if prime(2, m) == True:
                print(m)
        return increments(m+1, n)
    
    
increments(start,end)
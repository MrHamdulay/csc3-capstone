#vrmnic005
#assignment 8, question 4
import sys
sys.setrecursionlimit (30000)
from math import sqrt

def isprime(num, div=2):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % div == 0:
        return False
    elif div >= sqrt(num):
        return True
    else:
        return isprime(num, div+1)
    
def palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False
        
def check_nums(start, end):
    if start == end:
        return
    if isprime(start) and palindrome(str(start)):
        print(start)
    check_nums(start+1, end)
   
start = int(input("Enter the starting point N:\n"))
end = int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
check_nums(start, end+1)


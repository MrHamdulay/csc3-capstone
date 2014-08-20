#Program checking if numbers are prime and plaindromes
#Tyrone Arnold
#9 may 2014

import sys
sys.setrecursionlimit(30000)

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))

def num_reverse(n): #function to reverse a number
    return n if len(n) == 1 else n[-1] + num_reverse(n[:-1])


def if_palindrome(n): #function to check if palindrome
    if str(n) == num_reverse(str(n)):#if same forward as backward
        return True
    else:
        return False
    

def if_prime(n, count): #function to check if input is prime
    if n == 1: #1 is not prime
        return False
    elif count == int(n**(1/2)) + 1:
        return True
    else:
        if n % count == 0:
            return False
        else:
            return if_prime(n, count + 1) #recurse through input


palin = ''
def if_palin_prime(first, last): 
    global palin
    if first == last:
        if if_prime(first, 2) and if_palindrome(first):
            palin += str(first)
    else:
        if if_prime(first, 2) and if_palindrome(first):
            palin += str(first) + '\n'
            if_palin_prime(first + 1, last)
        else:
            if_palin_prime(first + 1, last)



print("The palindromic primes are:")
if_palin_prime(n, m)
print(palin)
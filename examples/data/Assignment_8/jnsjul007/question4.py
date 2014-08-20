#Julian van FRensburg
#Assignment 8 Q4
#9 May 2014

import math

import sys
sys.setrecursionlimit(30000)
def palindrome(word):
        if len(word) == 1:
                return word
        else: 
                return word[-1] + palindrome(word[:-1])
def check_palindrome(numb):
        if str(numb) == palindrome(str(numb)):
                return True
        else:
                return False
        
def check_prime(numb,div):
        if numb == 1:
                return False
        elif numb == 2:
                return True
        elif div >=math.sqrt(numb):
                if numb%div==0:
                        return False
                else:
                        return True
        elif numb%div==0:
                return False
        else:
                return check_prime(numb,div+1)
        
def find_palindrome(n,m):
        if n==m:
                if check_palindrome(n) and find_palindrome(n,2):
                        return str(n)
                else:
                        return ""
        else:
                if check_palindrome(n) and check_prime(n,2):
                        return str(n) + " " + find_palindrome(n+1,m)
                else:
                        return find_palindrome(n+1,m)
def print_list(pal):
        if len(pal)==1:
                return print(pal[0])
        else:
                print(pal[0])
                return print_list(pal[1:])

def main():
        n = int(input("Enter the starting point N:\n"))
        m = int(input("Enter the ending point M:\n"))
        word = find_palindrome(n,m)
        t = word.split(' ')        
        print("The palindromic primes are:")
        print_list(t)

main()
 
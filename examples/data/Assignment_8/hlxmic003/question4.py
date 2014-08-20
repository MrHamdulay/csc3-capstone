import math

import sys
sys.setrecursionlimit(10000)
def palindrome(word):
        if len(word) == 1:
                return word
        else: 
                return word[-1] + palindrome(word[:-1])
def check_drome(numb):
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
        
def find_drome(n,m):
        if n==m:
                if check_drome(n) and find_drome(n,2):
                        return str(n)
                else:
                        return ""
        else:
                if check_drome(n) and check_prime(n,2):
                        return str(n) + " " + find_drome(n+1,m)
                else:
                        return find_drome(n+1,m)
def print_list(pal):
        if len(pal)==1:
                return print(pal[0])
        else:
                print(pal[0])
                return print_list(pal[1:])

def main():
        n = int(input("Enter the starting point N:\n"))
        m = int(input("Enter the ending point M:\n"))
        word = find_drome(n,m)
        tote = word.split(' ')        
        print("The palindromic primes are:")
        print_list(tote)

main()
 
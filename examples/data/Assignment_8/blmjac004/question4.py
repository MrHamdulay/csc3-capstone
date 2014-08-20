"""Finding palindromic primes between two intergers
Jacqueline Blomendahl
9 may 2014"""

import sys
sys.setrecursionlimit(30000)

def palindrome(s):  #defining function
    if (ord(s[0]) - ord(s[len(s)-1])) == 0: #checking for same leter at begin and end
        return palindrome(s[1:len(s)-1]) #using recursion for the next letter
    else:
        return False
            

i = 2
def prime_number(n):
    global i
    if (n % i == 0 and n>i):
        return False
    if(n > i):
        i = i + 1
        return prime_number(n)
    if n==i:
        return True
    

start= input("Enter the starting point N:\n")
end= input("Enter the ending point M:\n")


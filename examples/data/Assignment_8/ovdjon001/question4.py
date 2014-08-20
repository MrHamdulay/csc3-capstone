""" Assingment 8, question3.py
by Jonathan Ovadia 
on 4th May 2014"""
import sys
import math
import question1
sys.setrecursionlimit (30000)

def main():
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    palindromic_primes(start,end)

def palindromic_primes(start,end):
    if start > end:
        return
    if question1.isPalindrome(str(start)) and isPrime(start):
        print(start)
    return palindromic_primes(start+1,end)



def isPrime(num,i =2):
    if i > math.sqrt(num)+1 and num!= 1 or num==2:
        return True
    elif num%i ==0 or num ==1:
        return False
    else:
        return isPrime(num,i+1)

if __name__ == "__main__": main()
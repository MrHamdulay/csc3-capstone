#finding palindromic primes within a range
#wayne de jager
#8 may 2014


import math
import sys
sys.setrecursionlimit(30000)

def numrange(): #creats a range of numbers to search between
    start=eval(input("Enter the starting point N:\n"))
    end=eval(input("Enter the ending point M:\n"))
    return start,end

def palin(num): #checks if first number mathces last
    if len(num)<=1:
        return True
    elif num[0]==num[-1]: #removes first and last
        return palin(num[1:-1]) #checks second and second last
    else:
        return False

def prime(num,div): #check if number is a prime number
    if num==0 or num==1:
        return False
    elif div>math.sqrt(num):
        return True
    elif num%div==0: #proves it is divisable, therefore not prime
        return False
    else:
        return prime(num,div+1) #checks next given number

def search(start,end):
    if start==end+1:
        return
    else:
        if palin(str(start))==True: #if the number is a palindrome continue
            if prime(start,2)==True: #if the number is a prime continue
                print(start)
        return search(start+1,end) #checks next number

def main(): #calls other functions
    start,end=numrange()
    print("The palindromic primes are:")
    search(start,end)

main()
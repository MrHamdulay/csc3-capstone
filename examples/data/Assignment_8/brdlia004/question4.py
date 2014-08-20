"""Palindromic Primes"""
#Liam Brodie
#BRDLIA004
#May 2014

import sys
sys.setrecursionlimit (30000)

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

PPList = ""

def prime(N,i):
    if N == 1 or N%2 == 0 and N>2:
        return False
    if i == N//2 or N == 3 or N == 2:
        return True    
    if N%i != 0 and N > 2:
        return prime(N, i+1)    
    else:
        return False
    
def palin(N):
    if len(str(N)) == 1:
        return True
    if len(str(N)) == 2 or len(str(N)) == 3: #Check if string is of length 2 or 3
        if str(N)[0] == str(N)[-1]:
            return True 
        if str(N)[0] != str(N)[-1]: #Check if the characters at the end and beginning of the string are equal
            return False                           
    if  len(str(N)) > 3:                        #Check if string is greater than length 3
        if str(N)[0] == str(N)[-1]:
            N = str(N)[1:len(str(N))-1]
            N = eval(N)
            return palin(N)
        if str(N)[0] != str(N)[-1]:          #Check if characters at end & begining of the string are unequal
            return False   

def PP(N,M):
    """Prints out the palindromic primes between two given integers"""
    global PPList
    if N == (M+1):
        print("The palindromic primes are:") 
        print(PPList)
    elif prime(N,2) and palin(N): 
        PPList += str(N) + "\n"
        N += 1
        return PP(N,M)
    else:
        N += 1
        return PP(N,M)        
        
    
PP(N,M)
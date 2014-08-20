#Phumelele Ndimande
#Assignment 8


import sys
sys.setrecursionlimit (30000)
import math

def palindrome(string):

    #checks if outer numbers are equal
    if string[:1] == string[-1:]:
        #Checks if there are no numbers
        if string == "":
            return True
        #checks if there are any numbers left
        else:
            return palindrome(string[1:-1])   
    else:
        return False
    
def prime(string,factor):
 
    if factor > 1: 
        if string % factor == 0: #not a prime if factor is 0
            return False
        else: 
            return prime(string,factor-2)
    else: #stops when factor is 1
        return True     
 
def palprime(start,end):
    
    if start <= end:
    
        if start % 2 == 0 and start > 2 or start == 1:
            return palprime(start+1, end)
        elif start == 2 or start == 3: 
            print(start)
            return palprime(start+1,end)
        else:
            factor = round(math.sqrt(start))
            if factor %2 ==0:
                factor+=1
            if prime(start,factor) and palindrome(str(start)): #Prints our prime or palindromic number
                print(start)
                return palprime(start+1,end)
            else: 
                return palprime(start+1,end)
    else:
        print()
        
def main():
    start = eval(input("Enter the starting point N:\n"))
    finish= eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")    
    palprime(start,finish)
        

main()
            

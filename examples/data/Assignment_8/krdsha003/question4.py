"""Assignment8 question 4
 find all palindromic primes between two integers supplied as input (start and end points are included).
 Shaheen Karodia
 KRDSHA003"""

import sys
sys.setrecursionlimit (30000)

import math


def prime(number, index):
    """check if number is a prime"""
    if number <2:    #any number less than two cannot be a prime
        return False
    
    if index>math.sqrt(number):    #a potential factor cannot be greater then the square root of a number #therefore this  means the number is prime 
        
        return True
    
    elif number%index==0: #if a number divided by another integer doesnt have a remainder, the number is not prime 
        return False
    
    else:
        return prime(number, index+1)  #recurse by checking a smaller set of divisors 
 
    
def palin(string):
    """checks if a string is a palindrome recursively"""
    
    if len(string)<2:    #Base case #if string is less than two it is automaticalllya palindrome
        return True
    
    elif string[0]==string[-1]:         #checks the first character against the last character in the string
            return palin(string[1:-1]) #return the function checking through a smaller string 
        
    else:
        return False    
    


def palin_prime(start, end):
    """check if all numbers between and including parametres are palindromic and prime"""
    
    if start==end:      #base case to ensue function stops recursing 
        if  palin(str(start))==True:

        
        
        
            if prime(start, 2)==True:  #invoke prime function to check if number is a prime 
                print (start)   
                
        
    else:
        if palin(str(start))==True: #check if number is palindrome
            if prime(start, 2)==True:    #invoke prime to check if the number is also a prime 
                print (start)       #only prints if number is palindrome and prime
        return palin_prime(start+1, end) #recurse by checking first prime in a smaller set of numners 
           
      
            
def main():
    #get start and end input from user 
    n=eval(input("Enter the starting point N:\n"))  
    m=eval(input("Enter the ending point M:\n"))  
    
    print("The palindromic primes are:")
    
    palin_prime(n, m)  #envoke paline_prime function 
    
    
    

if __name__=="__main__":
    main()           
                     
            
    
    
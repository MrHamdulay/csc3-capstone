#Shivam Ragoonaden
#RGNSHI002
#program to find palindromic primes 

import math
import sys
sys.setrecursionlimit (30000)

n = input("Enter the starting point N:\n")  #Get inputs from user

m = input("Enter the ending point M:\n")

def Pal(num):  #Reversing to check if Pal
    
    if num =="":  #Base case
        return ""
        
    elif num == " ":  #Space
        return " "
        
    else:
        return num[-1] + Pal(num[0:len(num)-1])  #Recursion to reverse string
    
def Prime(num, div):
    
    if num%div == 0:  #if divisible by a number
        if num != div: #Which is not itself
            return True  #It is not a prime
        
    if math.sqrt(num) < div:  #If the number you are dividing by is greater than the square root of the number
        return False  #Therefore it never passed through the above nested if statement, and it is a prime
        
    else:
        return Prime(num,div+1)  #Call the function again, with the divisor incremented by 1
    
def repeat(start,end):
    
    div = 2 #Start from 2 to test for prime numbers    
    
    if start == end:    #if it is the last number
        start = str(start)  
        x = Pal(start) #Call reversal function
        if start == x:  #If Palidrome
            start = int(start)  
            if Prime(start,div) == False:    #Check if prime 
                if x == "1":
                    print("",end = "") #Do nothing                    
                else:
                    print(x)
    else:
        start = str(start) #Same as above
        x = Pal(start)
        if start == x:
            start = int(start)
            if Prime(start,div) == False: 
                if x == "1":
                    print("",end = "") #Do nothing                
                else:
                    print(x)            
        start = int(start)
        start += 1  #Increase to next number in range
        start = str(start)
        repeat(start,m)  #Recall the repeat function, which does the process again for the next number

print("The palindromic primes are:")
repeat(n,m)     #Call function for first time
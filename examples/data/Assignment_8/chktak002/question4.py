import math
import sys
sys.setrecursionlimit (30000)

n = input("Enter the starting point N:\n")  

m = input("Enter the ending point M:\n")

def palindrome(s): 
    
    if s =="":  #Base case
        
        return ""
        
    elif s == " ":
        return " "
        
    else:
        return s[-1] + palindrome(s[0:len(s)-1])  #reverse string
    
def Prime(s, div):
    
    if s%div == 0:  
        if s != div: 
            return True  #if it is not a prime
        
    if math.sqrt(s) < div:  #checks in number is a prime without going through all the numbers in the range
        return False  
        
    else:
        return Prime(s,div+1) 
    
def repeat(start,end):
    
    div = 2 #all numers are divisible by 1, hence 1 can be ommited 
    
    if start == end:    #if it is the last number
        start = str(start)  
        x = palindrome(start) 
        if start == x:  
            start = int(start)  
            if Prime(start,div) == False:    #Check if prime 
                if x == "1":
                    print("",end = "")                     
                else:
                    print(x)
    else:
        start = str(start)
        x = palindrome(start)
        if start == x:
            start = int(start)
            if Prime(start,div) == False: 
                if x == "1":
                    print("",end = "")                
                else:
                    print(x)            
        start = int(start)
        start = start+1  #Increment number by 1
        start = str(start)
        repeat(start,m)  

print("The palindromic primes are:")
repeat(n,m)    

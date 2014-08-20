"""Keegan Naidoo
NDXKEE009
4 May 2014"""

import math
import sys
sys.setrecursionlimit (30000)

N=input("Enter the starting point N:\n")  #Input starting number

M=input("Enter the ending point M:\n")    #Input ending number

def Palindrome(No):  
    
    if (No==""):  #Base cases to check if empty string or space entered return empty string or space respectively
        
        return ""
        
    elif (No) == " ":  
        
        return " "
        
    else:
        
        return No[-1] + Palindrome(No[0:len(No)-1])  #Returns last letter of string and repeats function starting from first letter to second last letter
    
def Prime(No, div_No):
    
    if(No%div_No==0):  #Checks if the current number is divisible by any other number
        if (No!=div_No): #Checks if current number is not equal to current number
            return True  #Return true if it is divisible by another number
        
    if math.sqrt(No<div_No):  #Checks if the denomenator is greater than the square root of the number
        
        return False  
        
    else:
        
        return Prime(No,div_No+1)  #Loops through the numbers by adding 1
    
def Loop(current_no,Other_Number):
    
    div_No=2 
    
    if (current_no==Other_Number):    #Checks if the current number is the last number to allow the programme to stop
        
        current_no=str(current_no)  
        
        reverse=Palindrome(current_no) #Reverses string
        
        if(current_no==reverse):  #Checks if string is a palindrome
            
            current_no=int(current_no)  #Converts number to integer
            
            if(Prime(current_no,div_No)==False):    #Checks if the current number is a prime number
                
                if(reverse=="1"):
                    
                    print("",end = "") #If the number is one print the empty string   
                    
                else:
                    
                    print(reverse)
                    
    else:
        
        current_no = str(current_no) 
        
        reverse = Palindrome(current_no)
        
        if current_no == reverse:
            
            current_no = int(current_no)
            
            if Prime(current_no,div_No) == False: 
                
                if reverse == "1":
                    
                    print("",end = "")  
                    
                else:
                    
                    print(reverse)       
                    
        current_no = int(current_no)
        
        current_no += 1  #Allows programme to loop through the numbers
        
        current_no = str(current_no) #Converts current number to string
        
        Loop(current_no,M)  # Repeats the process for the other numbers

print("The palindromic primes are:")

Loop(N,M)    #Initiaites the process of calling all functions 
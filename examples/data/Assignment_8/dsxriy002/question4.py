#Question 4 - Assignment 8
#Riya Desai
#8 May 2014

import math

import sys

#define a limit that allows for higher numbers to be dealt with
sys.setrecursionlimit (30000) 


#define function "Pal"
def pal(s,test):
    if(len(str(s))!=1):
        
        #find the last number
        lastnumber=s%10  

        #add the last number to test
        test=test+str(lastnumber) 

        return pal((s-(s%10))//10,test) 

    else:

        return(test+str(s))



def prime(n,x,p):

    if(n==1):

        return (p+"Not")
    
    #find the square root of the function
    sq=int(math.sqrt(n)) 

    #find if it is not the square root
    if(x!=(sq+1)): 

        if(n%x!=0): 

            #call function again
            return prime(n,x+1,p) 

        else:

            return (p+"Not")

            

    

def method(n,m): 

    
    if n<=m:       

        tespPal=int(pal(n,"")) 
        
        #test to see if the number backwards == the number forwards 
        
        if tespPal==n: 
            
            #calls the prime function
            testPrime=prime(n,2,"") 

            if testPrime!="Not":

                print(n) 
                
                #calls the method of the next number
        method(n+1,m) 

        

        

if __name__== "__main__":

    n=eval(input("Enter the starting point N:\n"))

    m=eval(input("Enter the ending point M:\n"))

    print("The palindromic primes are:")

    method(n,m)

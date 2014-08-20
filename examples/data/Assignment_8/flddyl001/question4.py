"""find all palindromic primes between two integers supplied as input
Dylan Feldner-Busztin
8 May 2014"""

import sys
sys.setrecursionlimit (30000)

start = eval(input("Enter the starting point N:\n"))

end = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

#----------------------------------------------------------------------------------------------------------------------------------------

def travel(start,end):
    
    if start != end+1:

        divisor = 2
        countme = 0 
        prime(start,divisor,countme)

        if prime(start,divisor,countme) == 0:    
            
            palvalue = []
            test = str(start)            
            palindrome(test,start,palvalue)    
       

        travel(start + 1,end)

#----------------------------------------------------------------------------------------------------------------------------------------

#divisor = 2
#countme = 0

def prime(start,divisor,countme):
    
    if start != divisor:
        
        if start%divisor == 0:
            
            countme = countme + 1
            
        elif start%divisor != 0:
            
            countme = countme
            return prime(start,divisor + 1,countme)
            
    else: return countme


'''if prime(start,divisor,countme) == 0:    
    print("Prime!!")    
else:    
    print("Not Prime!")'''

#---------------------------------------------------------------------------------------------------------------------------------------

def palindrome(test,start,palvalue):
        
    if len(str(test)) == 0:   
    
        if str(start) == "".join(palvalue):
            
            print(start)
    
    else:
        palvalue.append(test[-1])        
        palindrome(test[0:len(test)-1],start,palvalue)
        
travel(start,end)
import math
import sys
sys.setrecursionlimit (30000)

global num


# Finding if palindrome using recursion    
# Brandon Hall (HLLBRA005)
# 09/05/2014

def palindrome(num):
    if (len(str(num)) < 2):
        return (True)
    elif(str(num)[0] == str(num)[-1]):
        return(palindrome(str(num)[1:(len(str(num))-1)]))
    else:
        return(False)


def check (start, end, prime, div):
    
    if start < end:
        if div < end:
            
            if  start % div == 0 and start != div:
                prime = False
                
            else:
                div += 1
                if palindrome(start):
                    print (start)
        start += 1
        check ( start, end, prime, div)
    
        
    


  

def Main():
    
    print("Enter the starting point N:")
    start = eval(input())
      
    print("Enter the ending point M:")
    end = eval(input())

    prime = True
        
    div = 2    
    check (start, end, prime, div)

Main()
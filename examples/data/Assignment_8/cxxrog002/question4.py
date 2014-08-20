"""palindromic primes between two numbers
Roger Cox
8 May 2014"""
import math
import sys
sys.setrecursionlimit (30000)
   
def if_pali(start) :    # check if palinomial
    x=False
    if start == 2 or start == 3 or start ==5 or start ==7 :
        return True
    elif (len(str(start)))/2>=1  : #only if the string is not in the centre stopping point
            start_st=str(start)
            if start_st[0]==start_st[-1] : #first char = last Char
                if_pali(start_st[1:-1]) # recursion of smaller string 
                #print(start_st)
                return True
                
            else:
                return False
def if_prime(start,endpt) : # check if prime
    if endpt<=math.sqrt(start) :
        if (start%endpt==0) :
            return False
        else:
            return if_prime(start,endpt+1)
            
    return True
def pali_prime (start, end): #go through all numbers between start and end
    if start <=end :
        if if_prime(start,endpt) and if_pali(start) :
            print(start)
            return pali_prime(start+1,end)
        else :
            return pali_prime(start+1,end)
        
endpt=2 # to start prime numbers division
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
pali_prime(start,end) 

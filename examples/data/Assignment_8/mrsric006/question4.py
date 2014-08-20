"""Palindromic primes 
Richard Marais
09/11/14"""

import sys,math
sys.setrecursionlimit (30000)

startno = int(input('Enter the starting point N:\n'))   #input for start number
if startno%2 == 0:
    startno+=1
    
endno = int(input('Enter the ending point M:\n'))   #input for end number
if endno%2 == 0:
    endno-=1

def CheckPrime(num,divisor,upperlim):   #check if prime number
    if num == 1:
        return False
    if num == 2 or num == 3:    #base case
        return True
    elif num%2 == 0:  # if even then false
        return False
    elif num%divisor != 0 and (divisor == upperlim or divisor == upperlim-1):  
        return True
    elif num%divisor != 0:                          #re-run the recursion if not divisible
        ans = CheckPrime(num,divisor+2,upperlim)
    else:
        return False         #else false
    return ans

def CheckPalindrome(palinstring,count,result):    #check for palindrome
    if (palinstring[count] == palinstring[len(palinstring)-count-1]    #if final parameters are met return true
        and count == len(palinstring)//2):
        result = True
    elif palinstring[count] == palinstring[len(palinstring)-count-1]: #keep running the recursion if the corresponding values are the same
        result = CheckPalindrome(palinstring,count+1,result)   
    else:
        result = False   #if some value doesnt correspond then return false
    return result

def CheckRange(num,upperlim):   #check both parameters
    if CheckPrime(num,3,math.ceil(math.sqrt(num))) == True:
        if CheckPalindrome(str(num),0,False):
            print(num)                  # if prime and palindrome then print
    if num == upperlim:
        return                      
    else:
        CheckRange(num+2,upperlim)          
print('The palindromic primes are:')
CheckRange(startno,endno)
        

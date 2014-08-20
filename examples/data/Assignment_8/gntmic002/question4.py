#Assignment 8.4
#Michael Gant
#05/05/2014




import sys
sys.setrecursionlimit (30000)

def Palin(sText):
    if len(sText) < 2:
        return True
    if sText[0] == sText[-1] :
        return Palin(sText[1:-1])
    return False

#checks if number is prime using recursion
def isPrime(num, div):
    if div == 1 and num != 1:
        return True
    elif (num%div == 0 and num != div) or (num == 1 ):
        return False
    else:
        return isPrime(num, div-1)

    
#checks if number is a palindrome and a prime number using recursion 
def PrimeNum(start, end):
    if end == start and Palin(str(start)):
        if isPrime(start, (start//2)+1) == True:
            print(start)
            
    elif Palin(str(end)) and isPrime(end, (end//2)+1) == True:
                PrimeNum(start, end-1)
                print(end)  

    elif end > start:
        PrimeNum(start, end-1) 
    
        
        

iStart = eval(input("Enter the starting point N:\n"))

iEnd = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
PrimeNum(iStart,iEnd)


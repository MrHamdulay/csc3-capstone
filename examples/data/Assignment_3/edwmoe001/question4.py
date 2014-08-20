#Palindromic prime calculator
import math
def pnumber(x):
    if str(x)==str(x)[::-1]:
        print(x)
    else:
        return

def prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True
            
def main():
    lower=int(input("Enter the starting point N:\n")) + 1
    upper=int(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for n in range(lower,upper):    
        if prime(n) == True:
            pnumber(n)
        else:continue
        
main()

        
          
        
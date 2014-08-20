#finding palindromes
#7 MAY 2014
#APHIWE baleni
import sys
sys.setrecursionlimit (30000)
import math
def pal_prime(start, end): 
        test=math.sqrt(start)
        if start==end:
                return ""
        elif start== 1:
                pal_prime(start+1, end)
        elif start==2 or start==3 or start==5 or start==7 or start==11 :
                        print(start) 
                        pal_prime(start+1, end)               
                
        elif start%2!=0 and start%3!=0 and start%5!=0 and start%7!=0 and start%11!=0 and start%13!=0 and start%17!=0 and start%19!=0 and start%23!=0 :
                        x= str(start)
                        if x== x[::-1]:
                                print(start) 
                                pal_prime(start+1, end)
                        else:
                                return pal_prime(start+1, end)
        else:
                return pal_prime(start+1, end)
        
start=input('Enter the starting point N:\n')
end=input('Enter the ending point M:\n')
start=eval(start)
end=eval(end)
c=pal_prime
print("The palindromic primes are:")
out=pal_prime(start, end)
if start==11 or end == 11:
        print(11)

        
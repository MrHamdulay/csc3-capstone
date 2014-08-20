# tarisai kalinde
# klntar002
# a program tlo find all palindromic primes using recursion within a range

import sys
sys.setrecursionlimit (30000)

# entering input
mini=eval(input('Enter the starting point N:\n'))
maxi=eval(input('Enter the ending point M:\n'))
mini=mini+1
divisor=2
accuprime=''
def prime(mini,maxi,accuprime,divisor):
    # base case
    if mini>=maxi:
        return 'list is'+accuprime
    
    elif mini<maxi:
        if divisor>=mini:
            return prime(mini+1,maxi,accuprime,divisor)
        else:
            if divisor<mini:
                if mini%divisor==0:
                    divisor+=1
                    return prime(mini+1,maxi,accuprime,divisor)
                else:
                    accuprime+=str(mini)
                    return prime(mini+1,maxi,accuprime,divisor)
                
print(prime(mini,maxi,accuprime,divisor))                
            
        


    
    
    



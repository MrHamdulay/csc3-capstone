"""Program to print all palindromic primes between two values input by user
Mick Perring
09 May 2014"""

import sys
sys.setrecursionlimit (30000)

import math

start = input("Enter the starting point N:\n")   # user inputs starting point
t = str(start)
end = input("Enter the ending point M:\n")   # user inputs end point

def palin_prime(start, end, div, palin, t):
    if start == ("") and end == (""):
        return("")
        
    elif div == -1 and start != (""):
        start = eval(start)
        end = eval(end)
        div = (int(math.sqrt(start)) + 1)
        t = str(start)
        return palin_prime(start, end, div, palin, t)
    elif start != ("") and start <= end:
        if t != "pal":
            if len(t) == 1:
                return palin_prime(start, end, div, palin, "pal")
            elif len(t) == 2:
                if t[0] == t[1]:
                    return palin_prime(start, end, div, palin, "pal")
                if t[0] != t[1]:
                    start += 1
                    div = (int(math.sqrt(start)) + 1)
                    t = str(start)
                    return palin_prime(start, end, div, palin, t)                    
            elif len(t) > 2:
                if t[0] == t[-1]:
                    return palin_prime(start, end, div, palin, t[1:-1])
                if t[0] != t[-1]:
                    start += 1
                    div = (int(math.sqrt(start)) + 1)
                    t = str(start)
                    return palin_prime(start, end, div, palin, t)        
        if t == "pal":
            if start == 2:
                palin += ("2\n")
                start += 1
                div = (int(math.sqrt(start)) + 1)
                t = str(start)
                return palin_prime(start, end, div, palin, t)
            elif start == 11:
                palin +=("11")
                start += 1
                div = (int(math.sqrt(start)) + 1)
                t = str(start)
                return palin_prime(start, end, div, palin, t)                
            elif start < 2:
                start += 1
                div = (int(math.sqrt(start)) + 1)
                t = str(start)
                return palin_prime(start, end, div, palin, t) 
            elif div == 1:
                palin += (str(start)+"\n")
                start += 1
                div = (int(math.sqrt(start)) + 1)
                t = str(start)
                return palin_prime(start, end, div, palin, t)            
            elif start%div == 0 and div != 1:
                start += 1
                div = (int(math.sqrt(start)) + 1)
                t = str(start)
                return palin_prime(start, end, div, palin, t)
            elif start%div != 0:
                div -= 1
                return palin_prime(start, end, div, palin, t)
            
    print("The palindromic primes are:\n" + palin)
    
palin_prime(start, end, -1, "", t)
import sys
import math
sys.setrecursionlimit (30000)

def primeFact (num, div):
    if math.sqrt(num) < div:
        return []
    if num % div == 0:
        return [div] + primeFact (num/ div, 2)
    return primeFact (num, div + 1)

def reverse(wrd):
    if wrd == "":
        return wrd
    else:
        return reverse(wrd[1:]) + wrd[0]
    

    
    
def listPrimes(start,end):
    if start>end:
        return 0
    else:
        if len(primeFact(start,2)) == 0 and start != 1 and reverse(str(start)) == str(start):
            print (start)
    return listPrimes(start+1, end)

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
listPrimes(n,m)





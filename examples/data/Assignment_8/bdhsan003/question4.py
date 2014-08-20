#Sandisha Budhal
#Bdhsan003

import sys
sys.setrecursionlimit (30000)

def rvs(wrd):
    if len(wrd) == 0 or len(wrd) == 1:
        return(wrd)
    else:
        return wrd[len(wrd) - 1] + rvs(wrd[1:len(wrd) - 1]) + wrd[0]

def checking():
    n = eval(input("Enter the starting point N:\n"))
    m = eval(input("Enter the ending point M:\n"))
    
   
    palinnumbers = []
    for i in range(n,m+1):
        if rvs(str(i)) == str(i):
            if str(i) != '1':
                palinnumbers.append(str(i))
           
   
    prime_num = []
    for j in (palinnumbers):
        prme = True
        for l in range(2,int(j)-1):
            if int(j)%l == 0:
                prme = False
                break
        if prme:
            prime_num.append(j)
                
    print("The palindromic primes are:")
    
   
    for a in range(len(prime_num)):
        print(prime_num[a])
            
checking()
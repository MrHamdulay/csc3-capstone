#question4
#Micaela Menegaldo   

import math

def primenumber(Nint):
    for i in range(2,(int(math.sqrt(Nint))+1),1):
        if Nint%i==0:
            break
        if Nint==M:
            break
    else:
        print(Nint)
        
    

def palindrome(N,M):
    while N<M:
        N+=1
        Nstring=str(N)
        reverse=Nstring[::-1]
        if Nstring==reverse:
            Nint=eval(Nstring)
            primenumber(Nint)
        else:
            continue


if __name__=='__main__':
    N=eval(input("Enter the starting point N: \n"))
    M=eval(input("Enter the ending point M: \n"))
    print("The palindromic primes are:")
    palindrome(N,M)
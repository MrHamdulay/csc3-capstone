import math
def pal(x):
    y=x
    a = 0
    while True:
        remainder=y%10
        y=y//10
        a = a*10 + remainder
        if y==0:
            break
    if a == x:
        return True
    else:
        return False 
def prime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if(x%i == 0):
            return False
    return True
def main():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(N+1,M):
        if(pal(i) and prime(i)):
            print(i)
main()    
       

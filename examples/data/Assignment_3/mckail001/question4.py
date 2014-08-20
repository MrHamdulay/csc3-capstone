import math
start=eval(input("Enter the starting point N:\n"))
finish=eval(input("Enter the ending point M:\n"))


def prime(number):
    trorfa=True    
    for i in range(2,number):
        if((number%i)==0):
            trorfa=False
            
    return trorfa        

def palin(start, end):
    print("The palindromic primes are:")
    for i in range(start+1, finish):
        if((i==int(str(i)[::-1]))):        
            if(prime(i)==True):
                print(i)
        
palin(start, finish)
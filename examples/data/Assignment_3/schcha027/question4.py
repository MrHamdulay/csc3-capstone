import math
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))


def primeCheck(number):
    tof=True    
    for i in range(2,number):
        if((number%i)==0):
            tof=False
            
    return tof        

def palinCheck(start, end):
    print("The palindromic primes are:")
    for i in range(start+1, end):
        if((i==int(str(i)[::-1]))):        
            if(primeCheck(i)==True):
                print(i)
        
palinCheck(start, end)
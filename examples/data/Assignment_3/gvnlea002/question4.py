import math
def question4():
    N= eval(input("Enter the starting point N:""\n"))
    M= eval(input("Enter the ending point M:""\n"))
    print("The palindromic primes are:")
    for i in range(N+1,M,1):
        v=str(i)
        reverse=v[::-1]
        if reverse==v:
            i=int(v)
            if findprime(i) == True:
                print(i)
            
def findprime(i):
    for j in range(2,int(math.sqrt(i))+1,1):
        if i%j==0:
            return False
    return True
        
question4()

    
    
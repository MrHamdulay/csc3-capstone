import math
def PPrime():
    starting = eval(input("Enter the starting point N:\n"))
    ending = eval(input("Enter the ending point M:\n"))
    prime = 0;
    pprime = ""
    
    print("The palindromic primes are:")

    for i in range(starting + 1,ending):
        for j in range(2,round(math.sqrt(i)) + 1):
            if i%j == 0:
                break
        else:
            prime = i
            pprime = str(prime)
            if pprime == pprime[::-1] and prime > 1:
                print(pprime)
                

PPrime()
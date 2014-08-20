import math

def Prime(var):
    if var < 2:
        return False
    if var == 2:
        return True
    if var%2==0:
        return False
    for x in range(3, int(math.sqrt(var))+1,2):
            if var % x == 0:
                    return False
    return True

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N,M,1):
    iReversed = int(str(i)[::-1])    
    if i == iReversed and Prime(i)==True and i!=N and i!=M :
        print(i)
            
#print(i)            
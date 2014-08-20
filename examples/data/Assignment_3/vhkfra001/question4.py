import math 
start = eval(input("Enter the starting point N:\n"))+1
end = eval(input("Enter the ending point M:\n"))-1

def palin(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
    
def prime(x):
    int(x)
    if x < 2: return False
    elif x % 2 == 0 and x > 2: 
        return False
    return all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))

print ("The palindromic primes are:")
for i in range (start, end+1):
    if palin(i) == False: continue
    if prime(i) == False: continue
    print(i) 
    

startnum = eval(input("Enter the starting point N:\n"))

endnum = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

def is_prime(z):
    if z < 2:
        return False
    elif z == 2:
        return True
    else: 
        for i in range (2,z):
            if z%i == 0:
                return False
        else:
            return True
            
for j in range(startnum+1,endnum):
    if str(j) == str(j)[::-1] and is_prime(j):
        print(j)
        
    
    
# Find palindromic primes between given values
# Michele Balestra BLSMIC004
# 23 March 2014

N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
    strI = str(i)
    if i==2:
        print(i)
    elif i==1: continue
    elif i%2==0:continue
    elif strI==strI[-1::-1]:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else: 
            print(i)
    else:
        pass
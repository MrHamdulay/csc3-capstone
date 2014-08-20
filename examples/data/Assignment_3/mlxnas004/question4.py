#nasha meoli
#program to find palindromic primes within range
#22nd march 2014
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
    
for i in range(N+1,M):
    reverse = str(i)[: :-1]
    if (2**(i-1))%i != 1 and i != 2:continue
    elif str(i) != reverse and i != 2 :continue
    else:
        print(i)   

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
N+=1
print("The palindromic primes are:\n", end='')
for i in range(N,M):
    M+=1
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        if (str(i)==str(i)[::-1]):
            print(i)
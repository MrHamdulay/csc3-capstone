#question4

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(N+1,M):
    if all(i%p!=0 for p in range(2,i)):
        if str(i)==str(i)[::-1]:
            print(i)
N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range (N+1, M):
    b = True
    for j in range (2,i//2+1):
        if(i%j == 0):
            b = False
            break
    if i != 1 and b and (str(i) == (str(i))[::-1]):
        print(i)
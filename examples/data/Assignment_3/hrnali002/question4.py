N = eval(input("Enter the starting point N:\n"))
M = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for l in range(N + 1 , M):
    for i in range(2,l):
        if l%i == 0:
            break
    else:
        if str(l) == (str(l))[::-1]:
            print(l)

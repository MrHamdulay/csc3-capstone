s = eval(input("Enter the starting point N:\n"))
e = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(s+1,e):
    n = str(i)
    r = n[::-1]
    if (n == r):
        d = 0
        for k in range(1,e+1):
            if i%k == 0:
                d+=1
        if d == 2:
            print(i)            
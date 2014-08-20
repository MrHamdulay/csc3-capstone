n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range (n+1, m):
    if str(i) == str(i)[::-1]:
        for j in range (2, i):
            print
            if (i/j).is_integer():
                break
        else:
            print(i)
        
    
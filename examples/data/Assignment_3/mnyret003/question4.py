x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
x+=1
primes = range(x, y)
print("The palindromic primes are:")
for i in primes:
    factors=range(2,i)
    for f in factors:
        if i%f == 0 :
            break
    else:
        if str(i) == str(i)[::-1] and str(i) !='1':
            print(i)
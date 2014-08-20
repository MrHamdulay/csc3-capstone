#Question 4, Assignment 3
#Tejasvin Bagirathi

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
test = 0
print("The palindromic primes are:")
for i in range(n+1, m):
    y=2
    x = str(i)
    revx = x[len(x):0:-1] + x[0]
    if x == revx:
        while y<i:
            test = i%y
            y+=1
            if test==0: break
        if test != 0:
            print(i)
        if i == 2:
            print(i)
        
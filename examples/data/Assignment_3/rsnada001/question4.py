#Adam Rosendorff
#RSNADA001
#CSC1015F - Assignment 3 - Question 4
n = eval(input('Enter the starting point N:\n'))
m = eval(input('Enter the ending point M:\n'))
print('The palindromic primes are:')
prime = True
for i in range(n+1,m):
    prime = True
    if i == 1:
        prime = False
    for j in range(2,i):
        if i%j==0:
            prime = False
            break
    if prime:
        if str(i) == str(i)[::-1]:
            print(i)

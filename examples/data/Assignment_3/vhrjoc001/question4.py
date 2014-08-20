import math

x=eval(input("Enter the starting point N:\n"))

y=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range((x+1),y):

    b=True

    for g in range(2,int(math.sqrt(i)+1)):

        if i%g==0:

            b=False

    if b:

        if str(i)[:]== str(i)[::-1]:

            print(i)
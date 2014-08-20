# Mpho Raselo
# question 4

a =eval(input("Enter the starting point N:\n"))
b =eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for num in range(a,b):
    if(str(num) == str(num)[::-1]):
        if(num>2):
            for a in range(2,num):
                y = True
                if(num%a==0):
                    y = False
                    break
            if y:
                print(num)
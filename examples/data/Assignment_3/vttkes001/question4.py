a = eval(input("Enter the starting point N:""\n"))
b = eval(input("Enter the ending point M:""\n"))
print("The palindromic primes are:")

a += 1
reverse = str(a)[::-1]

while a < b:
    if str(a)==reverse:
        for i in range(2,a):
            if a % i==0:
                break
        else:
            print(a)
    a += 1
    reverse = str(a)[::-1]
            
        
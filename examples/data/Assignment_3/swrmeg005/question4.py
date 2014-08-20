s=eval(input("Enter the starting point N:\n"))
e=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for a in range(2,number):
        if number%a==0:
            return False
    return True

for a in range(s+1,e):
    if prime(a)==True:
        a=str(a)
        if a==a[::-1]:
            a=int(a)
            print(a)
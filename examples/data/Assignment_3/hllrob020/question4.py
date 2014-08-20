N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

def is_prime(x):
    while x > 2:
        for i in range(2, x):
            if x % i == 0:
                return False
            else:
                return True
    else:
        return False

print("The palindromic primes are:")
    
for number in range(N+1, M):
    number=str(number)
    if number[::]==number[::-1] and is_prime(int(number))==True:
        print(number)        
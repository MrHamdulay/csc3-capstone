s = eval(input("Enter the starting point N:\n"))
e = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def is_prime(a):
    for i in range(2, a):
        if a%i==0:
            return False
    return True

for i in range(s+1, e):
    if i <= 1:
        continue
    if str(i) == str(i)[::-1]:
        if is_prime(i):
            print(str(i))
    

__author__ = 'George'
def isprime(number):
    prime = True
    for a in range(2,number):
        if number%a == 0:
            prime = False
            break
    return prime
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for a in range(start+1,end):
    if isprime(a):
        if str(a) == str(a)[::-1]:
            print(a)
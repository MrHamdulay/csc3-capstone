def is_prime(number):
    for j in range(2,number):
        if (number % j) == 0:
            return False
    return True

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

for i in range(start+1,end):
    num= str(i)
    reverse= num[::-1]
    if (num==reverse) and (is_prime(i)):
        print(i)

    
    
    
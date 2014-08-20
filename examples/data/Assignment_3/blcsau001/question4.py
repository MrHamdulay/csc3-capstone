num1 = eval(input("Enter the starting point N:\n"))

num2 = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else: 
        for i in range (2,x):
            if x%i == 0:
                return False
        else:
            return True
            
for number in range(num1+1,num2):
    if str(number) == str(number)[::-1] and is_prime(number):
        print(number)
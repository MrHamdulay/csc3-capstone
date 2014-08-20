#question 4

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(start+1,end):
    if(is_prime(i)):
        if(str(i) == (str(i))[::-1]):
            print(i)
    
    
    



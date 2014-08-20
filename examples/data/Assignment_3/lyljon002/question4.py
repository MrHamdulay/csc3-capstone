#22 March 2014
#Assignment 3
#LYLJON002


N = eval(input('Enter the starting point N:\n'))
M = eval(input('Enter the ending point M:\n'))
print("The palindromic primes are:")

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    
reverse = ''

for x in range(N + 1, M):
    if isPrime(x) == True:
        string = str(x)
        if x == eval(string[::-1]):
            print(x)
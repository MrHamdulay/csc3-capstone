n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

i=n+1

def isPrime(num):
    for j in range(2,int(num**0.5)+1):
        if num%j==0:
            return False

    return True

while(i<m):
    inverse = str(i)
    inverse=inverse[::-1]
    string = str(i)
    if((string==inverse) and isPrime(int(string)) and (int(string)!=1)):
        print(inverse)
    i+=1
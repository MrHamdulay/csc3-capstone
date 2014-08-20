import math
def prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return False
    return True
def palindromic(number):
    s=str(number)
    if s==s[::-1]:
        return True
    else:
        return False

def main():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(N+1,M):
        if prime(i) and palindromic(i):
            print(i)
main()


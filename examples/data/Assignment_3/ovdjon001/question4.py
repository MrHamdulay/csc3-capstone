def main():
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(start+1,end):
        if str(i) == str(i)[::-1] and isPrime(i) :
            print(i)

def isPrime(n):
    x = True
    for i in range(2,n):
        if n%i==0:
            x = False
    return x
        
main()
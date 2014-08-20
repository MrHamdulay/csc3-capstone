#question4
#Paul Truter
#27 march 2014



def main():
    N=eval(input("Enter the starting point N:\n"))
    M=eval(input("Enter the ending point M:\n")) 
    print("The palindromic primes are:")
    for i in range(N,M):
        if isPrime(i,N,M) and isPalindrome(i):
            print(i)

        
def isPrime(number,N,M):
    if N>0 and M>0:
        for j in range(2,number):
            if number%j==0:
                return False
            else: continue
        else:
            if N < number < M:
                return True

def isPalindrome(number):
    number=str(number)
    numberReverse=number[::-1]
    if number==numberReverse:
        return True
    else:
        return False 
main()
    
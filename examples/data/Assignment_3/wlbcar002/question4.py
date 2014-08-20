n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n")) 

    
def is_prime(no):
    prime = True
    for i in range(2,no):
        if no%i == 0:
            prime = False
    return prime

def final(n,m):
    print("The palindromic primes are:")
    for i in range(n+1, m):
        if str(i) == str(i)[::-1]:
            if is_prime(i) == True:
                print(i)
                

final(n,m)  

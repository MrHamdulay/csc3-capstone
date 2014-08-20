def isprime(x):
    if x == 1:
        return 0    
    for i in range(x-1,1,-1):
        if x%i == 0:
            return 0
    else: return 1
            

def main():
    n = eval(input("Enter the starting point N:\n"))
    m = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(n+1,m,1):
        rnum = str(i)
        if rnum[len(rnum)::-1] == rnum:
            if isprime(eval(rnum)) == 1:
                print(rnum)
main()        
    
N=int(input("Enter the starting point N:\n"))
M=int(input("Enter the ending point M:\n"))


def lolololol(word):
    rev=word[::-1]
    if rev==word:
        print(rev)


def palprime(N,M):
    for i in range(N+1,M):
        if i==1:
            continue
        div=2
        while div<i:
            rem=i%div
            if rem==0:
                break
            div+=1
        else:
            lolololol(str(i))
    
print("The palindromic primes are:")          
palprime(N,M)     
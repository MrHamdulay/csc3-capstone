N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
countDiv=1
def palindrome(N,M):
    display=""
    for n in range(N+1,M):
        k=str(n)
        if k[::-1]==str(n):
            display+=k+" "
    return display
    
print("The palindromic primes are:")
prime=""
check=False

def p(x):
    for i in range(2,x):
        if num%i==0: return 0
    else: return x
for n in palindrome(N,M).split():
    num=int(n)
    half=num//2
    if p(num):prime+=str(p(num))+" "
    
for d in prime.split():
    print(d)   



          
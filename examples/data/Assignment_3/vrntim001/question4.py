N = (input("Enter the starting point N:\n"))
M = (input("Enter the ending point M:\n"))
Nint = eval(N)
Mint = eval(M)
print("The palindromic primes are:")
def prime(i):
        for p in range(2,i):
                if i%p == 0:
                        return False
        return True
                 
for i in range(Nint+1,Mint):
        i = str(i)
        a = len(i)+1
        if i == i[-1:-a:-1] and prime(eval(i)):
                print(i)
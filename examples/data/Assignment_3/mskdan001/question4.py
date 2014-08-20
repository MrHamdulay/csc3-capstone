x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
def prime(r):
        for j in range(2,r):
                if r%j==0:
                        return False
        return True
def pali():
        for i in range(x,y):
                r=str(i)[::-1]
                if str(i)==r:
                        if prime(i) and i!=1:
                                print(r)
print("The palindromic primes are:")
pali()
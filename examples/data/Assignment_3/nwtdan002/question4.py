start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
def prime(a):
    if a<2:
        return False
    if a==2:
        return True
    for i in range(2,a):
        if a%i==0:
            return False
    return True

for i in range(start+1,end):
    if prime(i)==True:
        x=str(i)
        if i==eval(x[::-1]):
            print(i)
def primeNum(z):
    primeNum=True
    for i in range(2,z//2+1):
        if z%i==0:
            primeNum=False
            break
    return primeNum
def palindrome(z):
    z=str(z)
    if z==z[::-1]:
        return True
    else:
        return False
    
start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1,end):
    if i==1:
        continue
    if palindrome(i) == True:
        if primeNum(i) == True:
            print(i) 
        
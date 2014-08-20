def Primenom(n):
    if n%2==0 and n!=2:
        return False
    for j in range(3,n//2+2):
        if n%j==0:
            return False
        
    return True



X=eval(input("Enter the starting point N:\n"))
Y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(X+1,Y):
    if Primenom(i)==True and str(i)==str(i)[::-1]:
        print(i)
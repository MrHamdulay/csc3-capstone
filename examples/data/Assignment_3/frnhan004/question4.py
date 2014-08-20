s=eval(input("Enter the starting point N:\n"))
e=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:") #if incl. n here, it will write this line out everytime


for n in range(s+1,e):
    if all(n%i !=0 for i in range(2,n)): #if all not there, non primes print-all=if all elements of the iterable are true, return true
        if str(n) == str(n)[::-1]:
            print(n)
            

   
           
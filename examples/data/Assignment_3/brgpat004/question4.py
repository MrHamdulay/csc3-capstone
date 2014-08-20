start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1,end):
    x=True
    for j in range(2,i):
        if i%j==0:
            x=False
            break

            
    if x:
        string=str(i)

        if (string==string[::-1]):
            print(i)        

    
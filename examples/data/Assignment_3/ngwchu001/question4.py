print("Enter the starting point N:")
numb1=eval(input())
print("Enter the ending point M:")
numb2=eval(input())

print("The palindromic primes are:")
for x in range(numb1,numb2+1):
    for p in range(2,x):
        if(x%p==0):
            break
    else:
        if(str(x)==str(x)[::-1]):
                print(x)
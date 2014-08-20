x=eval(input("Enter the starting point N:""\n"))
y=eval(input("Enter the ending point M:""\n"))
print("The palindromic primes are:")
for i in range(x+1,y):
    rev=str(i)[: :-1]
    if (2**(i-1))%i!=1 and i!=2:continue
    elif str(i)!=rev and i!=2:continue
    else:
        print(i)
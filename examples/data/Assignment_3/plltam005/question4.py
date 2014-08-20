x=eval(input("Enter the starting point N:\n"))
y=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(x+1,y):
    forward=str(i)
    reverse=forward[::-1]
    if reverse==forward:
        for j in range(1,i+1):
            h=i%j
            factors=0
            if h==0:
                factors=factors+1
                while factors ==2:
                    print(i)
        
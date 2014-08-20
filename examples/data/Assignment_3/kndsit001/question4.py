x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
x+=1
print("The palindromic primes are:")
for i in range(x,y):
    z = True
    if(str(i) == str(i)[::-1]):
        if(i>2):
            for x in range(2,i):
                if(i%x==0):
                    z = False
                    break
                print
            if z:
                    print(i)
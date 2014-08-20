#Making an isosolese triangle of characters
i=eval(input("Enter the height of the triangle:\n"))
space=" "
for n in range(1,i+1):
        print(space*(i-1)+(2*n-1)*'*')
        i=i-1
    




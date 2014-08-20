h=eval(input("Enter the height of the triangle: \n"))

for i in range(1,h+1):
    space = h-1
    while space>=0:

        print(space*' ', end='')
        space = space - 1
        print(((2*i)-1)*'*') 
        i=i+1

    break

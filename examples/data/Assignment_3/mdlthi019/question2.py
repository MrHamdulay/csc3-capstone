h1=eval(input("Enter the height of the triangle:\n"))
h2=h1*2
space=(h2//2)-1
char="*"
for i in range(0,h2,2):
    print(" "*space,end='')
    print(char*(i+1))
    space = space-1
    
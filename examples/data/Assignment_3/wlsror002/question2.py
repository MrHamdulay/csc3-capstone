x=eval(input("Enter the height of the triangle:\n"))
y=1
for a in range(x):
    print((' '*(x-1))+('*'*y))
    y=y+2
    x=x-1
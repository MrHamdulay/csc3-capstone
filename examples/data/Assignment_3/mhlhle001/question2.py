def g():
    h=eval(input("Enter the height of the triangle:\n"))
    y=1
    x=1
    for i in range(1,h+1):
        print((h-x)*' '+"*"*y)
        x+=1
        y+=2
g()
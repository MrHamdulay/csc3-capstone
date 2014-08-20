x=eval(input('Enter the height of the triangle:\n'))
y=1
while x!=0:
    print(' '*(x-1), '*'*y, sep="")
    x=x-1
    y=y+2
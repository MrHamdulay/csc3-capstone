x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
def lid():
    a=z
    for i in range(z):
        print('|'*i+'+'+'-'*a+'-'*len(x)+'-'*a+'+'+'|'*i)
        a=a-1
def body():
    print(('|'*z+' '+x+' '+'|'*z+'\n')*y,end='')
def bottom():
    b=z-1
    c=1
    for j in range(z):
        print('|'*b+'+'+'-'*c+'-'*len(x)+'-'*c+'+'+'|'*b)
        b=b-1
        c=c+1
lid()
body()
bottom()
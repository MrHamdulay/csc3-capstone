def drawFrame(a,b,c,x):
    for i in range(c):
        print('|'*i,'+','-'*(x+2*(c-i)),'+','|'*i,sep='')
    for j in range(b):
        print('|'*c,a,'|'*c)
    for k in range(c-1,-1,-1):
        print('|'*k,'+','-'*(x+2*(c-k)),'+','|'*k,sep='')

a = input("Enter the message:\n")
b = eval(input("Enter the message repeat count:\n"))
c = eval(input("Enter the frame thickness:\n"))
x = len(a)

drawFrame(a,b,c,x)
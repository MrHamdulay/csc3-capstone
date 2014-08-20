message=input('Enter the message:\n')
repeat=eval(input('Enter the message repeat count:\n'))
thickness=eval(input('Enter the frame thickness:\n'))
y=thickness-1
x=len (message)
q=x+2
f=q+2*y
k=0
space=0
for i in range(y):
    print ("|"*k,'+','-'*f,'+', "|"*k,sep='')
    f=f-2
    k=k+1
if thickness>0:
    print('|'*y,'+','-'*q,'+','|'*y,sep='')
for i in range(0):
    print("|")
    print()
for i in range (repeat):
    print('|'*thickness," ",message," ",'|'*thickness, sep="")
if thickness>0:
    print('|'*y,'+','-'*q,'+','|'*y,sep='')  
f=f+2
space=thickness-2
for i in range(y):
    print ("|"*space,'+','-'*f,'+', "|"*space,sep='')
    f=f+2
    space=space-1
    

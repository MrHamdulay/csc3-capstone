message = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
meslen = len(message)
i=1
x = thick
while i<=thick:
    print('|'*(i-1),'+','-'*x,'-'*(meslen),'-'*x,'+','|'*(i-1),sep='')
    i+=1
    x-=1
for z in range(rep):
    print('|'*thick,message,'|'*thick)
x=0
while i>1:
    print('|'*(i-2),'+','-'*x,'-'*(meslen+2),'-'*x,'+','|'*(i-2),sep='')
    i-=1
    x+=1    

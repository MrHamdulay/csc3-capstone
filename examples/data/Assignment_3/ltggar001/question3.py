a=input('Enter the message:\n')
b=eval(input("Enter the message repeat count:\n"))
c=eval(input("Enter the frame thickness:\n"))
for i in range(0,c):  
    print('|'*i,'+',(len(a)+2*c-2*i)*'-','+','|'*i,sep='')
for i in range(0,b):
    print('|'*c,' ',a,' ','|'*c,sep='')
for i in range(c,0,-1):
    print('|'*(i-1),'+',(len(a)+2*c-2*(i-1))*'-','+','|'*(i-1),sep='')
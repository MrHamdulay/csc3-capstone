y=input("Enter the message:\n")
z=eval(input("Enter the message repeat count:\n"))
x=eval(input("Enter the frame thickness:\n"))
gap=0
r=x
for i in range(x):
    print('|'*gap,'+',(r-1)*'-',(len(y)+2)*'-',(r-1)*'-','+','|'*gap,sep='')
    gap+=1
    r-=1
for i in range(z):
    print(x*'|',y,x*'|')
for i in range(x):
    print('|'*(gap-1),'+',(r)*'-',(len(y)+2)*'-',(r)*'-','+','|'*(gap-1),sep='')
    gap-=1
    r+=1
    
    
   
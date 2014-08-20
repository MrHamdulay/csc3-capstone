a=input("Enter the message:"'\n')
b=eval(input("Enter the message repeat count:"'\n'))
c=eval(input("Enter the frame thickness:"'\n'))

#print('+','-'*15,'+',sep='')
x=0
p=len(a)+c*2
for i in range(c):
    print('|'*x,'+','-'*p,'+','|'*x,sep='')
    x=x+1
    p=p-2
for i in range(b):
    print('|'*c,a,'|'*c)
#e=c
#y=len(a)
x-=1
p+=2
for i in range(c):
    print('|'*x,'+','-'*p,'+','|'*x,sep='')
    x-=1
    p+=2
#print('+','-'*15,'+',sep='')
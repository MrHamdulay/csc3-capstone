m=input("Enter the message:\n")
x=eval(input("Enter the message repeat count:\n"))
y=eval(input("Enter the frame thickness:\n"))

for i in range(y):
    print('|'*i,'+','-'*((len(m)+2)+2*(y-i-1)),'+','|'*i,sep='')

for i in range(x):
    print('|'*y,' '+m+' ','|'*y,sep='')

for i in range(y-1,-1,-1):
    print('|'*i,'+','-'*((len(m)+2)+2*(y-i-1)),'+','|'*i,sep='')

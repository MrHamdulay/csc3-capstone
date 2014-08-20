msg=input("Enter the message:\n")
x=eval(input("Enter the message repeat count:\n"))
y=eval(input("Enter the frame thickness:\n"))
msg=" "+msg+" "
L=len(msg)

for i in range(y):
    print('|'*i,'+','-'*(L+2*(y-1-i)),'+','|'*i,sep="",end="\n")

for j in range(x):
    print(y*'|',msg,y*'|',sep="")
   
for k in range(y-1,-1,-1):
    print('|'*(k),'+','-'*((L)+2*(y-1-k)),'+','|'*(k),sep="",end="\n")
    

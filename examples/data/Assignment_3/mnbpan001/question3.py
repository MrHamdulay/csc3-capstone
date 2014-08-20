s=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))

for i in range(t):
    q=len(s)+2+2*t-2*(i+1)
    print('|'*i, '+', '-'*q,'+','|'*i,sep='')

for j in range(r):
    print('|'*t,s,'|'*t)

for i in range(t-1,-1,-1):
    q=len(s)+2+2*t-2*(i+1)
    print('|'*i, '+', '-'*q,'+','|'*i, sep='')

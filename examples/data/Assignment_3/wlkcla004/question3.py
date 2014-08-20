m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
l=len(m)
for i in range(t,0,-1):
    print((t-i)*'|','+', (l+2*i)*'-', '+', (t-i)*'|', sep='')
for i in range(r):
    print(t*'|', ' ', m, ' ', t*'|', sep='')
for i in range(1,t+1):
    print((t-i)*'|','+', (l+2*i)*'-', '+', (t-i)*'|', sep='')
    

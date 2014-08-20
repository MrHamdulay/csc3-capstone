y=input("Enter the message:\n")
z=eval(input("Enter the message repeat count:\n"))
x=eval(input("Enter the frame thickness:\n")) 
l=len(y)+2*x
e='+'
m=0
while m<x:
    print(m*'|'+e+'-'*(l-m*2)+e+m*'|')
    m+=1
for i in range (z):
    print('|'*x,y,'|'*x)
m=0
l=len(y)+2
while x>m:
    t=x-m-1
    print(t*'|'+e+'-'*(l+m*2)+e+t*'|')
    m+=1
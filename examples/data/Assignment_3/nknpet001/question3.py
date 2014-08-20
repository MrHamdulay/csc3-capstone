m=input("Enter the message:\n")
o=eval(input("Enter the message repeat count:\n"))
f=eval(input("Enter the frame thickness:\n"))
l = len(m)
p=l+f*2
cq=0
for i in range(f):
    print("|"*cq+"+"+"-"*p+"+"+"|"*cq)
    cq+=1
    p-=2
for i in range(o):
    print("|"*f,m,"|"*f)
p+=2
cq-=1
for i in range(f):
    print("|"*cq+"+"+"-"*p+"+"+"|"*cq)
    p+=2
    cq-=1
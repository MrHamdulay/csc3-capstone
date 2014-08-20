
n=input("Enter the message:\n")
m=eval(input("Enter the message repeat count:\n"))
l=eval(input("Enter the frame thickness:\n"))


k = len(n)
s=k+l*2
c=0
for i in range(l):
    print("|"*c+"+"+"-"*s+"+"+"|"*c)
    c+=1
    s-=2
    
for i in range(m):
    print("|"*l,n,"|"*l)
    
s+=2
c-=1

for i in range(l):
    print("|"*c+"+"+"-"*s+"+"+"|"*c)
    s+=2
    c-=1
#to frint a frame
m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
x=len(m)+2
y=2*(t-1)

for i in range(t):
    print("|"*i, end="")
    print("+","-"*x, end="",sep="")
    print("-"*y,"+","|"*i,sep="")
    y=y-2
    
for i in range(r):
    print("|"*t,m,"|"*t)
g=t-1 
u=0
for i in range(t,0,-1):
    print("|"*g,"+","-"*x,"-"*u,"+","|"*g, sep="")
    y=y+2
    g-=1
    u+=2
    
       
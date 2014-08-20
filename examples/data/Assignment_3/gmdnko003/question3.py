x= input("Enter the message:\n")
y= eval(input("Enter the message repeat count:\n"))
z= eval(input("Enter the frame thickness:\n"))
n=z-1 #own thing
s=z-1
t=1
o=1
p=z-1
q=1
r=z-1
if z>0:                         #lines for the top of the border
    print("+","-"*z,"-"*len(x),"-"*z,"+",sep="")
for i in range(n):              #lines for the rest of the upper border
    print("|"*o,"+","-"*(s),"-"*len(x),"-"*(s),"+","|"*o,sep="")
    p-=1
    o+=1
    s-=1
for i in range(y):              #lines for the message
    print("|"*z,x,"|"*z)
for i in range(n):              #lines for the rest of the lower border
    print("|"*r,"+","-"*(t),"-"*len(x),"-"*(t),"+","|"*r,sep="")
    r-=1
    q+=1
    t+=1
if z>0:                         #lines for the bottom of the border
    print("+","-"*z,"-"*len(x),"-"*z,"+",sep="")
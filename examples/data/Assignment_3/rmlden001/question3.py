a=input("Enter the message:\n")
q=len(a)

y=eval(input("Enter the message repeat count:\n"))
g=eval(input("Enter the frame thickness:\n"))
t=g
k=0
for i in range(g*2+y):
    if(i in range(0,g)):
        print("|"*i,"+","-"*(2*t+q),"+","|"*i,sep='')
        t-=1;
    elif(i in range(g+y, g*2+y)):
        print("|"*(g*2+y-i-1),"+","-"*(2*k+q+2),"+","|"*(g*2+y-i-1),sep='')
        k+=1
        
    elif(i in range(g, g+y)):
        print("|"*g,a,"|"*g)
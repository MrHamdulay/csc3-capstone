msg=input("Enter the message:\n")
n=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
y=(len(msg)+2*t)
a=0
for i in range(t):
    x="|"*a+"+"+"-"*y+"+"+"|"*a
    print(x)
    y=y-2
    a+=1
    
for i in range(n):
    print("|"*t,msg,"|"*t)

y=y+2
a+=-1 
for i in range(t):
    x="|"*a+"+"+"-"*y+"+"+"|"*a
    print(x)
    y=y+2
    a+=-1    
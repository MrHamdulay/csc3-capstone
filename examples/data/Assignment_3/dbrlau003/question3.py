x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count: \n"))
t=eval(input("Enter the frame thickness: \n"))
r=len(x)+(t+1)*2
if t>=1: 
    c=0
    for i in range(t):
        print(i*"|","+",(r-(2+c))*"-","+",i*"|", sep="")
        c+=2
for i in range (y):
    v=t*"|"
    print(v,x,v)
f=1
b=0
for i in range(t):
    print((t-f)*"|","+","-"*((r-2*t)+b),"+",(t-f)*"|",sep="")
    #c-=2
    f+=1
    b+=2

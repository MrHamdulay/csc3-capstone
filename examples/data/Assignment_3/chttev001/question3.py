#CHTTEVOO1
#Assignment 3
#Question 3

t=input("Enter the message: \n")
e=eval(input("Enter the message repeat count: \n"))
v=eval(input("Enter the frame thickness: \n"))
c=v-1
n=0
y=len(t)+2
x=len(t)+(2*v) #keep x outside loop otherwise it would keep resetting

for i in range (v):
    print("|"*n,"+",x*"-","+","|"*n,sep="")
    n=n+1
    x=x-2

for i in range (e):
    print(v*"|",t,v*"|")

for i in range (v):
    print("|"*c,"+",y*"-","+","|"*c,sep="")
    y=y+2
    c=c-1
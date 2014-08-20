
z=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
x=eval(input("Enter the frame thickness:\n"))
len1=len(z)

for i in range(0,x):
    print("|"*i,"+","-"*(len1+2*(x-i)),"+","|"*i,sep="")       
for i in range(y):
    print("|"*x,z,"|"*x,end="\n")
for i in range(x-1,-1,-1):
        print("|"*i,"+","-"*(len1+2*(x-i)),"+","|"*i,sep="")

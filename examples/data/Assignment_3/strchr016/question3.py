x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
x=("|"*z)+" "+x+" "+("|"*z)
for i in range(0,z):
    print("|"*i,"+","-"*(len(x)-2*(i+1)),"+","|"*i,sep="")
for j in range(0,y):
        print(x)
for c in range(z-1,-1,-1):
        print("|"*c,"+","-"*(len(x)-2*(c+1)),"+","|"*c,sep="")
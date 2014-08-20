#Mahnoor Ahmed
#AHMMAH001
#Framing a message

x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
a=(len(x))
b=((2*z)+a)
s=0
for i in range(z):
    print(("|"*s),"+","-"*b+"+",("|"*s),sep="")
    b=b-2
    s=s+1
for j in range(y):
    print(("|"*z)," ",x," ",("|"*z),sep="")
for k in range(z):
    a=a+2
    print(("|"*(z-1)),"+",("-"*(a)),"+",("|"*(z-1)),sep="")
    z=z-1
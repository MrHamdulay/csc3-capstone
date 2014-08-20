x=(input("Enter the message:\n"))
y=eval(input("Enter the message repeat count:\n"))
#quincy cele
#27 march 2014
#student number- clxqui001

z=eval(input("Enter the frame thickness:\n"))
for i in range (0,z):
    print(("|"*i),"+","-"*((len(x)+2*z)-2*i),"+",("|"*i),sep="")
for i in range(0,y):
    print(("|"*z),x,("|"*z))
for i in range(1,z+1):
    print(("|")*(z-i),"+","-"*((len(x)+2*z)-2*(z-i)),"+",("|"*(z-i)),sep="")
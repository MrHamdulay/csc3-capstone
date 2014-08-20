#MSLMDU002
#Masilela Mduduzi
#28 March 2014
x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
for i in range(z):
    print("|"*(i)+"+"+"-"*(len(x)+2*(z-i))+"+"+"|"*(i))
for i in range(y):
    print("|"*z,x,"|"*z)
for i in range(z-1,-1,-1):
    print("|"*(i)+"+"+"-"*(len(x)+2*(z-i))+"+"+"|"*(i))   

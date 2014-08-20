x = input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

length = len(x)
for i in range(z):
    print("|"*(i),"+","-"*(length+2*z-2*i),"+","|"*(i),sep='')
    
    
for i in range(y):
    print("|"*z,x,"|"*z,"\n", end='')


for i in range(z)[::-1]:
    print("|"*(i),"+","-"*(length+2*z-2*i),"+","|"*(i),sep='')
    
    



x=input("Enter the message: \n")
y=eval(input("Enter the message repeat count: \n"))
z=eval(input("Enter the frame thickness: \n"))
x=" "+x+" "

for i in range(1,z+1):
        print("|"*(i-1), "+", "-"*(len(x)+(2*z-2*i)), "+", "|"*(i-1), sep="")
        

i=1
while i<=y:
        print("|"*z, x, "|"*z, sep="")
        i+=1
       
for i in range(z,0, -1):
        print("|"*(i-1), "+", "-"*(len(x)+(2*z-2*i)), "+", "|"*(i-1), sep="")
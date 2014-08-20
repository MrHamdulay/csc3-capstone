x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
for i in range(1,z+1):
    print("|"*(i-1)+"+"+(len(x)+2*(z-i)+2)*"-"+"+"+"|"*(i-1))

for i in range(1,y+1):
    print("|"*z, x ,"|"*z)

for i in range(z,0,-1):
    print("|"*(i-1)+"+"+(len(x)+2*(z-i)+2)*"-"+"+"+"|"*(i-1))

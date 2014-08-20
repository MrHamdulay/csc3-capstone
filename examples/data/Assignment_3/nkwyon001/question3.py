x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
s=len(x)
for i in range(z):
    print("|"*i+"+"+(z-i)*'-'+s*'-'+(z-i)*'-'+"+"+"|"*i)
for i in range(y):
        print("|"*z+' '+x+' '+"|"*z)
for i in range(z):
    print("|"*(z-i-1)+"+"+(i+1)*'-'+s*'-'+(i+1)*'-'+"+"+"|"*(z-i-1))
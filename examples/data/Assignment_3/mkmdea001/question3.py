
l=input("Enter the message:\n")

r=eval(input("Enter the message repeat count:\n"))

f=eval(input("Enter the frame thickness:\n"))
l
x = len(l)
y = x + f*2 
z = 0
for j in range(f):
    print("|"*z + "+" + y*"-" + "+" + "|"*z)
    y = y - 2
    z += 1

for i in range(r):
    print("|"*f,l,"|"*f)
    
y = y + 2
z = z-1
    
for j in range(f):
         
    print("|"*z + "+" + y*"-" + "+" + "|"*z)
    y = y +2
    z = z - 1








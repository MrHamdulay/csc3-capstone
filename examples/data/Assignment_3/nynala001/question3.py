x=input("Enter the message:\n")

y=eval(input("Enter the message repeat count:\n"))

z=eval(input("Enter the frame thickness:\n"))

l = len(x)
u = l + z*2 
c = 0
for j in range(z):
    print("|"*c + "+" + u*"-" + "+" + "|"*c)
    u = u - 2
    c += 1

for i in range(y):
    print("|"*z,x,"|"*z)
    
u = u + 2
c = c-1
    
for j in range(z):
         
    print("|"*c + "+" + u*"-" + "+" + "|"*c)
    u = u +2
    c += -1   


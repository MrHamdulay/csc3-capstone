x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))

k =(z*"|"+" "+x+" "+z*"|")
q = len(x)+(z*2)
v=0
for j in range(-1,z-1,1):
    print((j+1)*"|"+"+"+q*"-"+"+"+(j+1)*"|")
    q=q-2

for i in range(0,y,1):    
    print(k)

for j in range(z-1,-1,-1):
    q=q+2
    print((j)*"|"+"+"+q*"-"+"+"+(j)*"|")
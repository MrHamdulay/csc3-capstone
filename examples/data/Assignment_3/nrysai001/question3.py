m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
l= len(m)

for f in range(0,t):
    print("|"*f+"+"+(2*(t-f)+l)*"-"+"+"+"|"*f)
    
for j in range(0,r):
    print("|"*t,m,"|"*t)
k=2
for f in range(t,0,-1):
    print("|"*(f-1)+"+"+(l+k)*"-"+"+"+"|"*(f-1))
    k+=2
    
    
    
    

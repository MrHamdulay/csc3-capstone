m=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))
l= len(m)

for i in range(0,t):
    print("|"*i+"+"+(2*(t-i)+l)*"-"+"+"+"|"*i)
    
for j in range(0,r):
    print("|"*t,m,"|"*t)
k=2
for i in range(t,0,-1):
    print("|"*(i-1)+"+"+(l+k)*"-"+"+"+"|"*(i-1))
    k+=2
    
    
    
    

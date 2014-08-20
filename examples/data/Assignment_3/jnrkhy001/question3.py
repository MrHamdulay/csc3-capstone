x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
minus = (len(x)+2*z)
vert = 0


for i in range(z):
    print("|"*vert+"+"+"-"*minus+"+"+"|"*vert)
    vert+=1
    minus-=2
    
for j in range(y):
    print("|"*2,x,"|"*2)
    
vert=1
minus = (len(x)+2*z)-2
    
for k in range(z):
    print("|"*vert+"+"+"-"*minus+"+"+"|"*vert)
    vert-=1
    minus+=2
    
    
    


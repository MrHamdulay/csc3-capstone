x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
    
def body():
    for i in range(y):
        print("|"*z, " ", x, " ", "|"*z, sep="")
        
def top():
    c=0
    for i in range(z, 0, -1):
        a=(len(x))
        print("|"*c, "+", "-"*(a+(i*2)), "+", "|"*c, sep="")
        c+=1
        
def bottom():
    c=z-1
    b=(len(x))
    for i in range(z):
        
        print("|"*c, "+", "-"*(b+2), "+", "|"*c, sep="")
        c-=1
        b+=2
        
    
top()
body()
bottom()
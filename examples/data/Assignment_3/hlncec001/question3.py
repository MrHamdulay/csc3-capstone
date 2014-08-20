def function():
    life=input("Enter the message:\n")
    t=eval(input("Enter the message repeat count:\n"))
    k=eval(input("Enter the frame thickness:\n"))
    y=len(life)+(2*k)
    z=0
    for i in range(k):
        print("|"*z,"+","-"*y,"+","|"*z,sep="")
        y=y-2
        z+=1
    for x in range(t):
        print("|"*k," ",life," ","|"*k,sep="")
    y=y+2
    z-=1
    for m in range(k):
        print("|"*z,"+",y*"-","+","|"*z,sep="")
        y+=2
        z-=1
        
        
        
function()
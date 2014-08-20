#question3
message=input("Enter the message:\n")
x=len(message)
repeat=eval(input("Enter the message repeat count:\n"))
ft =eval(input("Enter the frame thickness:\n"))
    
for h in range(ft):
    print(h*"|","+",(x+(2*ft))*"-","+",h*"|",sep="")
    x-=2
    
for a in range (repeat):
    print(ft*"|",message,ft*"|")
    
    
for b in range(ft,0,-1):
        print((b-1)*"|","+",((x+2)+(2*ft))*"-","+",(b-1)*"|",sep="")
        x+=2
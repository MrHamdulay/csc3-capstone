m=input("Enter the message:\n")
rc=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))

lng=len(m)+t*2
def border():   
        
    for i in range (0,t,1):
        print("|"*(i),"+", "-"*(lng-(2*i)),"+","|"*(i) ,sep ="") 
        
    for j in range(rc):
        print("|"*t," ",m," ","|"*t, sep="")
        
    for k in range(t,0,-1):
        print("|"*(k-1),"+","-"*(lng-(2*k-2)),"+","|"*(k-1), sep ="")
        
border()
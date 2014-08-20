def message():
    message=input("Enter the message:\n") 
    count=eval(input("Enter the message repeat count:\n"))
    thickness=eval(input("Enter the frame thickness:\n"))
    
    dash=len(message)+2*thickness
    for i in range(thickness):
        print("|"*i,"+","-"*dash,"+","|"*i,sep="")
        dash=dash-2
    
    for i in range(count):
        print("|"*thickness,message,"|"*thickness) 
    
    dash2=len(message)+2
    for i in range(thickness,0,-1):
        print("|"*(i-1),"+","-"*dash2,"+","|"*(i-1),sep="")
        dash2=dash2+2
message()
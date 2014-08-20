message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
width=len(message)+(thick)*2
dash = 0
for i in range(0,thick,1):
    
    print("|"*dash,"+","-"*width,"+","|"*dash,sep="")
    dash +=1
    width -=2
    
for i in range(0,repeat,1):
    print("|"*thick," ",message," ","|"*thick,sep="",end="\n")
    
dash-=1
width+=2
for i in range(0,thick,1):
        
    print("|"*dash,"+","-"*width,"+","|"*dash,sep="")
    dash -=1
    width +=2
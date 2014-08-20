def frame():
        
        message=input("Enter the message:\n")
        length=len(message)
        repeat=eval(input("Enter the message repeat count:\n"))
        thickness=eval(input("Enter the frame thickness:\n"))
        dash=(thickness)*2+length
        
        dash3=(thickness)*2+length
        for row in range(thickness):
                print("|"*row,"+","-"*dash,"+","|"*row,sep="")
                dash=dash-2
        dash2=dash
        
        for i in range(repeat):
                print("|"*thickness,message,"|"*thickness)
        for j in range (thickness-1,-1,-1):
                if(thickness>1):
                        dash2 = dash2 + 2
                        print("|"*j,"+","-"*dash2,"+","|"*j,sep="")
                        
                else:
                        print("+","-"*dash3,"+",sep="")
        
frame()

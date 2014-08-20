#cherise Dube 
#28 March 2014
#Programe to create a message in a frame

message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness= eval(input("Enter the frame thickness:\n"))

def framedwords():  #This function will create the outter most frame (the dashes)
    dash= len(message)
    for h in range(thickness):
        dash=dash+2
    return dash
   
line="" 
dash=framedwords()
for i in range(thickness):  #Creating the top part of the frame
        print(line,"+","-"*dash,"+",line, sep="")
        line+="|"
        dash-=2
        
 
for j in range(repeat): #Creating part of frame with message
        print("|"*thickness,message,"|"*thickness)

line=thickness-1    #Creating bottom part of frame.   
dash=len(message)+2
for g in range(thickness):
        print(line*"|","+","-"*dash,"+",line*"|", sep="")
        line-=1
        dash+=2  

    
    
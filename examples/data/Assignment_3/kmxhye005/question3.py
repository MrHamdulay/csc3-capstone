#question 3

def boxmessage (message, repeat, frame_thickness):
    
    if frame_thickness>0:
        print ("+","-"*(len(message)+2*frame_thickness),"+",sep="") 
        count = 1 
        dcount = 1 
        
        #1st loop for top frame
        for i in range (frame_thickness-1): #frame - 1
            print ("|"*(count),"+",(len(message)+2*frame_thickness-2*dcount)*"-","+","|"*(count),sep="")
            count = count + 1 #increasing count by 1 every loop
            dcount = dcount + 1 #increasing dcount by 1 every loop
        
        #2nd loop for message
        for i in range (repeat):
            print ("|"*frame_thickness,message,"|"*frame_thickness)
        
        #3rd loop for bottom frame 
        count=frame_thickness-1
        dcount=frame_thickness-1
        
        #1st loop for top frame
        for i in range (frame_thickness-1): #frame - 1
            print ("|"*(count),"+",(len(message)+2*frame_thickness-2*dcount)*"-","+","|"*(count),sep="")
            count = count - 1 #decreasing count by 1 every loop
            dcount = dcount - 1 #decreasing count by 1 every loop
        if frame_thickness>0:
            print ("+","-"*(len(message)+2*frame_thickness),"+",sep="")
            
        

message = input ("Enter the message:\n")
repeat = eval (input("Enter the message repeat count:\n"))
frame_thickness = eval (input("Enter the frame thickness:\n"))
        
            
             
boxmessage(message, repeat, frame_thickness)
        
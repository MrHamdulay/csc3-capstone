#question 3

message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
frame=eval(input("Enter the frame thickness:\n"))

def awesome(message, repeat, frame):
    #Frame 1 is two characters greater than the input string
    #Printing the string messages would work quite well.
    #The repeat is how many lines of the top frame you will print.
    #For example, repeat = 2, you will need to print 2 lines worth of frame
    #at the top and two at the bottom. The 2 also reflects the lines you would need
    #at the sides of the message itself.
    
    if frame>0:
        print("+","-"*(len(message)+2*frame),"+",sep="") 
        #counters help a lot ;)
        count=1
        dcount=1
        #first loop for top frame
        for i in range(frame-1): #it is frame-1 because we have printed one of the frames already. range(frame) will result in an extra unneccessary line.
            print("|"*(count),"+",(len(message)+2*frame-2*dcount)*"-","+","|"*(count),sep="")
            count+=1
            dcount+=1
        #second loop for message
        for i in range(repeat):
            print("|"*frame,message,"|"*frame)
        #third loop for bottom frame which is the inverse of the top loop
        count=frame-1
        dcount=frame-1
        #first loop for top frame
        for i in range(frame-1): #it is frame-1 because we have printed one of the frames already. range(frame) will result in an extra unneccessary line.
            print("|"*(count),"+",(len(message)+2*frame-2*dcount)*"-","+","|"*(count),sep="")
            count-=1
            dcount-=1
        if frame>0:
            print("+","-"*(len(message)+2*frame),"+",sep="")
            
        
        
            
            
                    
awesome(message, repeat, frame)
        
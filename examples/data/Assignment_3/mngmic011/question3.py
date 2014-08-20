#question3
#Micaela Menegaldo

message=input("Enter the message: \n")
repeat=eval(input("Enter the message repeat count: \n"))
frame=eval(input("Enter the frame thickness: \n"))

framewidth=frame
extra=framewidth*2-2

for i in range(1,frame+1):
    print("|"*(frame-framewidth),"+","-"*(len(message)+2+extra),"+","|"*(frame-framewidth), sep='')
    frame=frame+1
    extra=extra-2    

for i in range(repeat):
    print("|"*framewidth, message, "|"*framewidth)
    
extra=0

for i in range(1,framewidth+1):
    print("|"*(framewidth-1),"+","-"*(len(message)+2+extra),"+","|"*(framewidth-1), sep='')
    framewidth=framewidth-1
    extra=extra+2 

    
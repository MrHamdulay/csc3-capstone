#BLKAT005
#Kate Bell
# 23 March 2014

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

#print top part of frame
for i in range(frame):
    print("|"*i, "+","-"*(len(message)+2*frame-2*i),"+","|"*i,sep="")
    
#print message repeats 
for j in range(repeat):
    print("|"*frame," ",message," ","|"*frame,sep="")
    
#print bottom part of frame 
for k in range(1,frame+1):
    print("|"*(frame-k), "+","-"*(len(message)+2*frame-2*(frame-k)),"+","|"*(frame-k),sep="")